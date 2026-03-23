import config
from curl_cffi import requests
import json
import hashlib
import os
import re
from concurrent.futures import ThreadPoolExecutor
from html import unescape

import pytz, datetime
timestamp = datetime.datetime.now(pytz.UTC).isoformat()


today = datetime.datetime.today()
monday = today - datetime.timedelta(days=today.weekday())
monday_date = monday.date().isoformat()



folder = fr'D:\PAGE_SAVE\3619\{config.run_date}\pdp'
if not os.path.exists(folder):
    print('Folder not exists! Creating...')
    os.makedirs(folder, exist_ok=True)
else:
    print('Folder already exists:', folder)



def pdp_data(data):

    url = data.get("Platform url of the SKU")
    _id = data['_id']
    pl_hash_id = data['hashid']
    product_title = data['product_title']
    if not url:
        print(f"No URL found in document with _id: {data.get('_id')}")
        return

    print('Fetching Data ..........!!!!!')

    combined_string = url + str(pl_hash_id)
    hash_utf81 = combined_string.encode('utf8')
    r_url_hash_id = str(int(hashlib.md5(hash_utf81).hexdigest(), 16) % (15 ** 15))
    file_name = f"{r_url_hash_id}.html"
    path = os.path.join(folder, file_name)

    cookies = {
        '_bb_locSrc': 'default',
        'x-channel': 'web',
        '_bb_aid': 'MjkxMzA4NDUzMA==',
        '_bb_cid': '1',
        '_bb_vid': 'MTExNjk4MjQ1ODc2MDQxMTg4Ng==',
        '_bb_nhid': '7427',
        '_bb_dsid': '7427',
        '_bb_dsevid': '7427',
        '_bb_bhid': '',
        '_bb_loid': '',
        'csrftoken': 'wneYkefPd5wzjWqFaXOV2WDhtWOTOmV9AJFFOQKTu9Qd3wlwcqycy72iXNOFIbcd',
        'isintegratedsa': 'true',
        'jentrycontextid': '10',
        'xentrycontextid': '10',
        'xentrycontext': 'bbnow',
        '_bb_bb2.0': '1',
        'is_global': '1',
        '_bb_addressinfo': '',
        '_bb_pin_code': '',
        '_bb_sa_ids': '19224',
        '_is_tobacco_enabled': '1',
        '_is_bb1.0_supported': '0',
        '_bb_cda_sa_info': 'djIuY2RhX3NhLjEwLjE5MjI0',
        'is_integrated_sa': '1',
        'is_subscribe_sa': '0',
        'bb2_enabled': 'true',
        'csurftoken': '3gCdxA.MTExNjk4MjQ1ODc2MDQxMTg4Ng==.1770644547551.ZnolL7245KvGAfdQBaoJMEn/M84UbSl7EJBx6LB1xyg=',
        'bigbasket.com': '085e3eac-ad20-4339-8138-21c99b0a7366',
        'ufi': '1',
        '_gcl_au': '1.1.437003713.1770644551',
        'adb': '0',
        'jarvis-id': '18f72f0f-a41b-40d7-905b-ac9fb21cd4b2',
        '_ga': 'GA1.2.700042212.1770644554',
        '_gid': 'GA1.2.1173822440.1770644555',
        '_gat_UA-27455376-1': '1',
        '_fbp': 'fb.1.1770644557724.306379071119437157',
        '_ga_FRRYG5VKHX': 'GS2.1.s1770644554$o1$g1$t1770644582$j32$l0$h0',
        'ts': '2026-02-09%2019:13:16.424',
    }

    headers = {
        'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
        'accept-language': 'en-US,en;q=0.9',
        'cache-control': 'max-age=0',
        'priority': 'u=0, i',
        'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'document',
        'sec-fetch-mode': 'navigate',
        'sec-fetch-site': 'same-origin',
        'sec-fetch-user': '?1',
        'upgrade-insecure-requests': '1',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
        # 'cookie': '_bb_locSrc=default; x-channel=web; _bb_aid=MjkxMzA4NDUzMA==; _bb_cid=1; _bb_vid=MTExNjk4MjQ1ODc2MDQxMTg4Ng==; _bb_nhid=7427; _bb_dsid=7427; _bb_dsevid=7427; _bb_bhid=; _bb_loid=; csrftoken=wneYkefPd5wzjWqFaXOV2WDhtWOTOmV9AJFFOQKTu9Qd3wlwcqycy72iXNOFIbcd; isintegratedsa=true; jentrycontextid=10; xentrycontextid=10; xentrycontext=bbnow; _bb_bb2.0=1; is_global=1; _bb_addressinfo=; _bb_pin_code=; _bb_sa_ids=19224; _is_tobacco_enabled=1; _is_bb1.0_supported=0; _bb_cda_sa_info=djIuY2RhX3NhLjEwLjE5MjI0; is_integrated_sa=1; is_subscribe_sa=0; bb2_enabled=true; csurftoken=3gCdxA.MTExNjk4MjQ1ODc2MDQxMTg4Ng==.1770644547551.ZnolL7245KvGAfdQBaoJMEn/M84UbSl7EJBx6LB1xyg=; bigbasket.com=085e3eac-ad20-4339-8138-21c99b0a7366; ufi=1; _gcl_au=1.1.437003713.1770644551; adb=0; jarvis-id=18f72f0f-a41b-40d7-905b-ac9fb21cd4b2; _ga=GA1.2.700042212.1770644554; _gid=GA1.2.1173822440.1770644555; _gat_UA-27455376-1=1; _fbp=fb.1.1770644557724.306379071119437157; _ga_FRRYG5VKHX=GS2.1.s1770644554$o1$g1$t1770644582$j32$l0$h0; ts=2026-02-09%2019:13:16.424',
    }

    params = {
        'nc': 'cl-prod-list',
        't_pos_sec': '1',
        't_pos_item': '1',
        # 't_s': '20W Type C Mobile Charger Adapter%2C Fast Charging For Android%2C iPhone - RAAP M20',
        't_s': product_title,
    }


    if os.path.exists(path):
        print(f"PDP already saved: {path}")
        with open(path, "r", encoding="utf-8") as f:
            content = f.read()
    else:
        print(f"Fetching new PDP: {url}")
        response = requests.get(url, params=params, cookies=cookies, headers=headers, impersonate="chrome120")
        if response.status_code == 200:
            content = response.text
            with open(path, "w", encoding="utf-8") as f:
                f.write(content)
        else:
            print(f"Failed to fetch PDP: {response.status_code}")
            return

    match = re.search(
        r'<script id="__NEXT_DATA__" type="application/json">\s*({.*?})\s*</script>',
        content,
        re.DOTALL
    )

    ratings_count = reviews_count = avg_rating = ''
    breadcrumbs_slug = ''

    if not match:
        print("No __NEXT_DATA__ script found → probably Cloudflare, login page or broken HTML")
        ratings_count = reviews_count = avg_rating = ''
    else:
        try:
            json_data = json.loads(match.group(1))
        except json.JSONDecodeError as e:
            print(f"JSON in __NEXT_DATA__ is invalid: {e}")
            ratings_count = reviews_count = avg_rating = ''
        else:
            rnrData = (json_data.get("props", {}).get("pageProps", {}).get("dySectionsData", {}).get("rnrData", {}))
        if not rnrData:
            print("rnrData section missing in JSON")
            ratings_count = reviews_count = avg_rating = ''
        else:
            rating_stats = rnrData.get("rating_stats") or {}  # <-- crucial line
            ratings_count = rating_stats.get("ratings_count", '')
            reviews_count = rating_stats.get("reviews_count", '')
            ratings = rating_stats.get("avg_rating", '')



        breadcrumbs = (json_data.get("props", {}).get("pageProps", {}).get("productDetails", {}).get("children", [{}])[0].get("breadcrumb", []))
        if breadcrumbs:
            breadcrumbs = ' > '.join([item.get('slug', '') for item in breadcrumbs])
        else:
            breadcrumbs = ''



        tabs = json_data.get('props', {}).get('pageProps', {}).get('productDetails', {}) \
            .get('children', [{}])[0].get('tabs', [])

        description_paragraphs = []
        raw_html = ""
        for tab in tabs:
            title = tab.get('title', '').strip()
            if title.lower() == 'about the product':
                raw_html = tab.get('content', '')
                break
        if not raw_html:
            description_text = ""
        else:
            try:
                html_content = json.loads(f'"{raw_html}"')
            except:
                html_content = raw_html
            html_content = re.sub(r'<style[\s\S]*?</style>', '', html_content, flags=re.IGNORECASE)
            html_content = re.sub(r'<script[\s\S]*?</script>', '', html_content, flags=re.IGNORECASE)
            paragraphs = re.findall(r'<(p|div)[^>]*>([\s\S]*?)</\1>', html_content, flags=re.IGNORECASE)
            if not paragraphs:
                text = re.sub(r'<[^>]+>', ' ', html_content)
                text = re.sub(r'\s+', ' ', text).strip()
                if len(text) > 20:
                    description_paragraphs.append(text)
            else:
                for _, p_content in paragraphs:
                    clean_text = re.sub(r'<[^>]+>', '', p_content)
                    clean_text = unescape(clean_text)
                    clean_text = clean_text.replace('\n', ' ').replace('\r', '')
                    clean_text = re.sub(r'\s+', ' ', clean_text).strip()
                    if len(clean_text) > 10:
                        description_paragraphs.append(clean_text)
            description_text = ', '.join(description_paragraphs)



        product = json_data.get('props', {}).get('pageProps', {}).get('productDetails', {}).get('children', [{}])[0]
        usp_raw = product.get('usp', '').strip()
        usp_items = []
        if usp_raw:
            usp_items = [item.strip()for item in re.split(r'[,\|•·–—]\s*', usp_raw)if len(item.strip()) > 2]


        features_items = []
        for tab in product.get('tabs', []):
            if tab.get('title', '').strip().lower() == 'features':
                html = tab.get('content', '')
                html = re.sub(r'<style.*?>.*?</style>', '', html, flags=re.DOTALL | re.IGNORECASE)
                html = unescape(html)
                li_items = re.findall(r'<li[^>]*>(.*?)</li>', html, flags=re.DOTALL | re.IGNORECASE)
                if li_items:
                    features_items = [
                        re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', li)).strip()
                        for li in li_items
                        if li.strip()
                    ]
                    break
                p_items = re.findall(r'<p[^>]*>(.*?)</p>', html, flags=re.DOTALL | re.IGNORECASE)
                if p_items:
                    features_items = [
                        re.sub(r'\s+', ' ', re.sub(r'<[^>]+>', '', p)).strip()
                        for p in p_items
                        if p.strip()
                    ]
                    break
                text = re.sub(r'<[^>]+>', ' ', html)
                text = re.sub(r'\s+', ' ', text).strip()
                lines = re.split(r'\n|\r\n?|<br\s*/?>|•|·|\d+\.\s*|-\s+', text)
                features_items = [line.strip() for line in lines if len(line.strip()) > 3]
                break
        final_list = features_items or usp_items or []
        # final_output = ' , '.join(final_list)



        out = {}
        out['category'] = "Home > " + breadcrumbs
        out['detail_data'] = {
            'run_date': config.run_date_1,
            'upc_retailer_id': '',
            'model': '',
            'manufacturer_part': '',
            'sell_price': data.get('sell_price'),
            'sold_by': 'Bigbasket',
            'shipped_by': 'Bigbasket',
            'description': description_text,
            'bullets': final_list,
            'images': data.get('images'),
            'videos': '',
            'documents': '',
            'rating': ratings,
            'reviews': reviews_count,
            'product_view_360': ''
        }
        out['rating_count'] = ratings_count
        out['pdp_page_save_path'] = path
        out['timestamp'] = timestamp
        out['week_run_date'] = monday_date


        try:
            config.collection_1.update_one({'_id': _id}, {'$set': out})
            print(f"Inserted to DB____________!!!")
        except Exception as e:
            print(f'DB Insert Error: {e}')


    config.collection_1.update_one({"_id": _id}, {"$set": {"status": "done"}})
    print(f"Keyword '{data.get('product_title')}' status updated to DONE")


if __name__ == '__main__':
    while True:
        all_pending_keyword = config.input.distinct('keyword', {'bigbasket_status':'running'})
        if not all_pending_keyword:
            print('DONEE')
            break

        for keyword in all_pending_keyword:
            for _ in range(10):
                data = list(config.collection_1.find({'keyword': keyword, 'status': 'pending'}))
                if len(data) == 0:
                    print("Updated Code here")
                    try:
                        config.input.update_one({'keyword': keyword, 'bigbasket_status': 'running'},{'$set':{'bigbasket_status': 'done'}})
                    except Exception as e:
                        print(e)
                    break
                with ThreadPoolExecutor(max_workers=1) as exe:
                    exe.map(pdp_data, data)