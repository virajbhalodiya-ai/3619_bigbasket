import datetime
import json

import pandas as pd
import re

import requests


# ---------------------------------
# FLATTEN NESTED detail_data
# ---------------------------------
def flatten_detail_data(df: pd.DataFrame):
    if "detail_data" in df.columns:
        detail_df = pd.json_normalize(df["detail_data"])
        detail_df.columns = ["detail_data." + col for col in detail_df.columns]
        df = pd.concat([df.drop(columns=["detail_data"]), detail_df], axis=1)
    return df


# ---------------------------------
# FAST QA FUNCTION (Vectorized)
# ---------------------------------
def qa_check_products(df: pd.DataFrame):
    qa_report = {}

    if df.empty:
        return {"error": "DataFrame is empty"}

    def add_issue(column, issue, mask):
        if mask.sum() == 0:
            return
        rows = df.loc[mask]
        qa_report.setdefault(column, []).append({
            "issue": issue,
            "count": int(mask.sum()),
            "sample_ids": rows["id"].astype(str).head(5).tolist()
        })

    # -------------------------
    # REQUIRED FIELDS
    # -------------------------

    required_fields = [
        "rank", "id", "product_title", "Pincode",
        "availability", "msrp",
        "Platform url of the SKU",
        "detail_data.run_date",
        "detail_data.sell_price",
        "detail_data.shipped_by",
        "detail_data.sold_by"
    ]

    for col in required_fields:
        if col in df.columns:
            mask = df[col].isna() | (df[col].astype(str).str.strip() == "")
            add_issue(col, "missing", mask)

    # -------------------------
    # TYPE CHECKS
    # -------------------------

    # rank numeric
    rank_numeric = pd.to_numeric(df["rank"], errors="coerce")
    add_issue("rank", "not_integer", rank_numeric.isna())

    # id string
    add_issue("id", "not_string", ~df["id"].map(type).eq(str))

    # product_title string
    add_issue("product_title", "not_string", ~df["product_title"].map(type).eq(str))

    # Pincode str/int
    add_issue("Pincode", "invalid_type",
              ~df["Pincode"].map(lambda x: isinstance(x, (str, int))))

    # -------------------------
    # ENUM CHECK
    # -------------------------

    valid_availability = ["Available", "Out of Stock"]
    add_issue("availability", "invalid_enum",
              ~df["availability"].isin(valid_availability))

    # -------------------------
    # URL CHECKS
    # -------------------------

    url_cols = [
        "main_image",
        "thumbnail_image_url",
        "detail_page_images"
    ]

    for col in url_cols:
        if col in df.columns:
            mask = df[col].notna() & ~df[col].str.startswith("http", na=False)
            add_issue(col, "not_http_url", mask)

    add_issue("Platform url of the SKU", "missing_or_not_http",
              df["Platform url of the SKU"].isna() |
              ~df["Platform url of the SKU"].str.startswith("http", na=False))

    # -------------------------
    # NUMERIC CHECKS
    # -------------------------

    msrp_numeric = pd.to_numeric(df["msrp"], errors="coerce")
    add_issue("msrp", "not_numeric", msrp_numeric.isna())
    add_issue("msrp", "negative_price", msrp_numeric < 0)

    if "detail_data.sell_price" in df.columns:
        sell_numeric = pd.to_numeric(df["detail_data.sell_price"], errors="coerce")
        add_issue("detail_data.sell_price", "not_numeric", sell_numeric.isna())
        add_issue("detail_data.sell_price", "negative_price", sell_numeric < 0)

    # -------------------------
    # DATE FORMAT
    # -------------------------

    if "detail_data.run_date" in df.columns:
        mask = ~df["detail_data.run_date"].astype(str).str.match(
            r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}", na=False
        )
        add_issue("detail_data.run_date", "invalid_format", mask)

    # -------------------------
    # STRING REQUIRED FIELDS
    # -------------------------

    for col in ["detail_data.shipped_by", "detail_data.sold_by"]:
        if col in df.columns:
            mask = df[col].isna() | (df[col].astype(str).str.strip() == "")
            add_issue(col, "missing_or_blank", mask)

    # -------------------------
    # LIST CHECK
    # -------------------------

    if "detail_data.bullets" in df.columns:
        bullets_col = df["detail_data.bullets"]

        # 1️⃣ Not list
        not_list_mask = bullets_col.notna() & ~bullets_col.map(lambda x: isinstance(x, list))

        # 2️⃣ Empty / NA / Blank string
        empty_mask = (
                bullets_col.isna() |
                (bullets_col.astype(str).str.strip().isin(["", "NA", "None"]))
        )

        add_issue("detail_data.bullets", "not_list", not_list_mask)
        add_issue("detail_data.bullets", "missing_or_blank", empty_mask)

    # -------------------------
    # DUPLICATE CHECKS
    # -------------------------

    # add_issue("id", "duplicate_id", df["id"].duplicated(keep=False))
    # add_issue("rank", "duplicate_rank", df["rank"].duplicated(keep=False))

    return qa_report


# ---------------------------------
# MAIN
# ---------------------------------
if __name__ == '__main__':
    import db_config as db

    db_obj = db.DbConfig()

    api_platform_dict = {
        'amazon_fresh': "amazon_fresh_data",
        'blinkit': "blinkit_data",
        'bigbasket': "bigbasket_data",
        'zepto': "zepto_data",
        'instamart': "instamart_data",
    }

    query = {'timestamp': {'$lt': '2026-02-19', '$gte': '2026-02-10'}}

    # 🔥 IMPORTANT: Use Projection (FASTER Mongo Query)
    projection = {
        "rank": 1,
        "id": 1,
        "product_title": 1,
        "brand": 1,
        "category": 1,
        "Pincode": 1,
        "availability": 1,
        "msrp": 1,
        "main_image": 1,
        "thumbnail_image_url": 1,
        "detail_page_images": 1,
        "Platform url of the SKU": 1,
        "detail_data": 1
    }

    data = db_obj.mydb[api_platform_dict['blinkit']].find(query, projection)

    df = pd.DataFrame(list(data))   # Convert cursor to list once

    # Flatten nested JSON
    df = flatten_detail_data(df)

    # Clean column names
    df.columns = df.columns.str.strip()

    # Run QA
    check_data = qa_check_products(df)

    if check_data:

        error_list = []

        for column, issues in check_data.items():
            for issue_obj in issues:
                error_list.append({
                    "column": column,
                    "issue": issue_obj["issue"],
                    "count": issue_obj["count"],
                    "sample_ids": ", ".join(issue_obj["sample_ids"])
                })

        df_main = [error_list]
        label_arr = [f"Issue {i + 1}" for i in range(len(error_list))]

    else:
        df_main = [{'status': 'API is working successfully!!!'}]
        label_arr = ['success']

    to_arr = ['meet.patel@xbyte.io']
    cc_arr = [

        # 'somya.singh@xbyte.io',
        # 'bhavin.dhanwani@xbyte.io',
        # 'hit.borsaniya@xbyte.io',
        # # 'alpesh.khunt@xbyte.io', 'bhavesh.parekh@xbyte.io', 'anil.prajapati@xbyte.io',
        # 'harsh.k.patel@xbyte.io',
        # 'amit.yadav@xbyte.io',

    ]
    bcc_arr = []

    try:
        payload = {
            'df_main': df_main,
            'df_name': '<b>API Details</b>',
            # 'df_header': json.loads(summary_df.to_json(orient='records')),
            # 'df_header_name': 'Rule Summary',
            'label_arr': label_arr,
            'project_name': '[Auto QA][XB:3619] Quick Commerce India API',
            'client_name': '-',
            'graph_flag': 'No',
            # 'client_io_flag': 'No',
            'client_io_flag': 'Yes',
            # 'Alert_code': '0',
            'Alert_code': '3801',

            'pro_active_subject': f'[XB:3619] Quick Commerce India API Auto QA - {datetime.datetime.now().strftime("%d-%m-%Y")}',
            'graph_type': 'bar',
            'to_arr': to_arr,
            'cc_arr': cc_arr,
            'bcc_arr': bcc_arr,
        }
        data = json.dumps(payload)
        resp = requests.post(
            url="http://192.168.0.39:5020/exclusive_graph/",
            data=data,
            headers={"Content-Type": "application/json"}
        )
        print(f"Mail sent: {resp.text}\nwith status code: {resp.status_code}")
    except Exception as e:
        print(f"Error in sending mail: {e}")