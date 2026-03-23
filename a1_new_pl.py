import json
import base64
from curl_cffi import requests
from parsel import Selector
from urllib.parse import quote_plus
import config
import os
import hashlib
import sys

try:
    start = int(sys.argv[-2])
    end = int(sys.argv[-1])
except:
    start = 0
    end = 1000


folder = fr'D:\PAGE_SAVE\3619\{config.run_date}\pl'
if not os.path.exists(folder):
    print('Folder not exists! Creating...')
    os.makedirs(folder, exist_ok=True)
else:
    print('Folder already exists:', folder)


def get_data():

    pending_keywords = list(config.input.find({"bigbasket_status": "pending", "api_key":'9noci65oeogu990eag2zlrzu1'}).skip(start).limit(end))
    print(f'Keyword fetch with the status pending : {len(pending_keywords)}')
    if not pending_keywords:
        print("No pending keywords found.")

    for kw_entry in pending_keywords:
        keyword = kw_entry['keyword']
        keyword_id = kw_entry['_id']
        zipcode = kw_entry['zipcode']
        input_hashid = kw_entry['hashid']
        api_key = kw_entry['api_key']
        input_date = kw_entry['input_date']

        product_count = 0
        total_inserted = 0
        page = 1
        rank_counter = 1

        sess = requests.Session()
        keyword_quote = quote_plus(keyword)

        url1 = "https://www.bigbasket.com/"

        headers1 = {
            "host": "www.bigbasket.com",
            "connection": "keep-alive",
            "upgrade-insecure-requests": "1",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
            "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
            "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "sec-ch-ua-platform": "\"Windows\"",
            "sec-fetch-site": "none",
            "sec-fetch-mode": "navigate",
            "sec-fetch-user": "?1",
            "sec-fetch-dest": "document",
            # "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9"
        }

        response1 = sess.get(url1, headers=headers1, impersonate="chrome")
        resp1 = Selector(text=response1.text)


        inline_json0 = resp1.xpath('//script[contains(text(),"_bb_vid")]/text()').get('')
        json_load1 = json.loads(inline_json0)

        _bb_vid = json_load1['props']['visitorCookies']['_bb_vid']


        url2 = "https://www.bigbasket.com/places/v1/places/autocomplete/"

        querystring2 = {
            "inputText": f"{zipcode}",
        }

        headers2 = {
            "host": "www.bigbasket.com",
            "connection": "keep-alive",
            "sec-ch-ua-platform": "\"Windows\"",
            "common-client-static-version": "101",
            "x-integrated-fc-door-visible": "false",
            "x-tracker": "238a4f4a-85b2-48fb-9331-c2f97077cd96",
            "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
            "sec-ch-ua-mobile": "?0",
            "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
            "content-type": "application/json",
            "x-entry-context": "bbnow",
            "x-entry-context-id": "10",
            "x-channel": "BB-WEB",
            "accept": "*/*",
            "sec-fetch-site": "same-origin",
            "sec-fetch-mode": "cors",
            "sec-fetch-dest": "empty",
            "accept-encoding": "gzip, deflate, br, zstd",
            "accept-language": "en-US,en;q=0.9",
        }

        response2 = sess.get(url2, headers=headers2, params=querystring2, impersonate="chrome")

        json_load2 = json.loads(response2.text)

        all_sugg = json_load2['predictions']
        if all_sugg:
            description = all_sugg[0]['description']
            placeId = all_sugg[0]['placeId']
            mainText = all_sugg[0]['mainText']
            secondaryText = all_sugg[0]['secondaryText']


            url3 = "https://www.bigbasket.com/places/v1/places/details/"

            querystring3 = {
                "placeId": placeId,
                "token": "ecd18b36-a06c-413b-8adb-44a7d10bbbfe",
                "xArm": "1278",
                "yArm": "242"
            }
            response3 = sess.get(url3, headers=headers2, params=querystring3, impersonate="chrome")

            json_load3 = json.loads(response3.text)

            lat = json_load3['geometry']['location']['lat']
            lng = json_load3['geometry']['location']['lng']

            lat_lng_str = f"{lat}|{lng}"

            lat_lng_base64 = base64.b64encode(lat_lng_str.encode()).decode()

            # ======= API ======================

            url = "https://www.bigbasket.com/listing-svc/v2/products"

            querystring = {
                "type": "ps",
                "slug": f"{keyword}",
                "page": f"{page}",
                "bucket_id": "92"
            }

            headers = {
                "host": "www.bigbasket.com",
                "connection": "keep-alive",
                "osmos-enabled": "true",
                "sec-ch-ua-platform": "\"Windows\"",
                "common-client-static-version": "101",
                "x-integrated-fc-door-visible": "false",
                "x-tracker": "1ed01663-6486-4e37-ab59-0f3bbf77b27a",
                "sec-ch-ua": "\"Google Chrome\";v=\"143\", \"Chromium\";v=\"143\", \"Not A(Brand\";v=\"24\"",
                "sec-ch-ua-mobile": "?0",
                "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36",
                "content-type": "application/json",
                "x-entry-context": "bbnow",
                "x-entry-context-id": "10",
                "x-channel": "BB-WEB",
                "accept": "*/*",
                "sec-fetch-site": "same-origin",
                "sec-fetch-mode": "cors",
                "sec-fetch-dest": "empty",
                "accept-language": "en-US,en;q=0.9",
                "cookie": f"_bb_locSrc=default; x-channel=web; _bb_vid={_bb_vid}; _bb_lat_long={lat_lng_base64}"
            }


            while True:

                cache_key = f"{keyword}-{zipcode}-{page}"
                hash_utf8 = cache_key.encode("utf8")
                r_url_hash_id = str(int(hashlib.md5(hash_utf8).hexdigest(), 16) % (10 ** 10))
                file_path = os.path.join(folder, f"{r_url_hash_id}.html")

                if os.path.exists(file_path):
                    print(f"Page already saved: {file_path}")
                    with open(file_path, "r", encoding="utf-8") as f:
                        content = f.read()
                else:
                    print(f"Fetching page from URL: {url}")
                    response = sess.get(url, headers=headers, params=querystring, impersonate="chrome")
                    print(f"Status code: {response.status_code}")

                    try:
                        if response.status_code in [204,303]:
                            config.input.update_one({"_id": keyword_id}, {"$set": {"bigbasket_status": "not_found"}})
                            print("Status Updated To not_found __________________________________!!!!!")
                            break

                        elif response.status_code == 200:
                            content = response.text
                            with open(file_path, "w", encoding="utf-8") as f:
                                f.write(content)
                        else:
                            print('Exiting - No more pages or page blocked.')
                            break
                    except Exception as e:
                        print(e)

                json_data = json.loads(content)
                main_data = json_data.get('tabs', [])



                has_products = False
                for i in main_data:
                    if i.get('product_info', {}).get('products'):
                        has_products = True
                        break

                if not has_products:
                    print("No products found. Moving to next keyword.")
                    break

                for i in main_data:
                    search_info = i.get('search_info', [])
                    # Make sure it's a list
                    if isinstance(search_info, dict):
                        search_info = [search_info]  # wrap single dict in a list
                    elif not isinstance(search_info, list):
                        continue  # skip if not list or dict

                    not_found = False
                    for msg in search_info:
                        if msg.get('display_message'):
                            config.input.update_one({"_id": keyword_id}, {"$set": {"bigbasket_status": "not_found"}})
                            print("Status Updated To not_found __________________________________!!!!!")
                            not_found = True
                            continue

                    if not_found:
                        continue

                    for prd_data in i.get('product_info', {}).get('products', []):
                        if product_count >= 100:
                            break

                        id = prd_data.get('id')
                        product_title = prd_data.get('desc')
                        weight = prd_data.get('w')
                        product_url = prd_data.get('absolute_url')
                        sku_id = prd_data.get('requested_sku_id')

                        image_urls = [img.get('s', '') for img in prd_data.get('images', []) if 's' in img]
                        all_image_url = "  ,  ".join(image_urls)
                        first_image_url = image_urls[0] if image_urls else ""

                        brand_name = ""
                        brand_data = prd_data.get('brand')
                        if isinstance(brand_data, list):
                            for brand in brand_data:
                                brand_name = brand.get('name', "")
                                break
                        elif isinstance(brand_data, dict):
                            brand_name = brand_data.get('name', "")
                        else:
                            brand_name = brand_data

                        availability = "Out of Stock"
                        availability_data = prd_data.get('availability')
                        if isinstance(availability_data, list):
                            for available in availability_data:
                                stock = available.get('avail_status', "")
                                if stock == "001":
                                    availability = "Available"
                                    break
                        elif isinstance(availability_data, dict):
                            stock = availability_data.get('avail_status', "")
                            if stock == "001":
                                availability = "Available"
                        else:
                            if availability_data == "001":
                                availability = "Available"

                        mrp = ""
                        discount_in_per = ""
                        selling_price = ""
                        discount_data = prd_data.get('pricing', {}).get('discount')
                        if isinstance(discount_data, list):
                            for discount in discount_data:
                                if isinstance(discount, dict):
                                    mrp = discount.get('mrp', "")
                                    discount_in_per = discount.get('d_text', "")
                                    selling_price = discount.get('subscription_price', "")
                                    break
                        elif isinstance(discount_data, dict):
                            mrp = discount_data.get('mrp', "")
                            discount_in_per = discount_data.get('d_text', "")
                            selling_price = discount_data.get('subscription_price', "")
                        else:
                            discount_in_per = str(discount_data)

                        raw_key = f"{id}-{keyword}-{zipcode}-{input_date}"
                        hash_id = hashlib.md5(raw_key.encode()).hexdigest()[:12]

                        out = {}
                        out['rank'] = rank_counter
                        out['input_date'] = input_date
                        out['input_hashid'] = input_hashid
                        out['input_zipcode'] = zipcode
                        out['keyword'] = keyword
                        out['api_key'] = api_key
                        out['hashid'] = hash_id
                        out["id"] = id
                        out["product_title"] = product_title
                        out["brand"] = brand_name
                        out["main_image"] = first_image_url
                        out["Pincode"] = zipcode
                        out["availability"] = availability
                        out["msrp"] = mrp
                        out["thumbnail_image_url"] = first_image_url
                        out["detail_page_images"] = all_image_url
                        out["Platform url of the SKU"] = 'https://www.bigbasket.com' + product_url
                        out["sell_price"] = selling_price
                        out['images'] = len(image_urls)
                        out['weight'] = weight
                        out['sku_id'] = sku_id
                        out['discount_in_per'] = discount_in_per
                        out['pl_page_save_path'] = file_path
                        out['status'] = 'pending'

                        if config.collection_1.find_one({"hashid": hash_id}):
                            print("Duplicate entry skipped!", product_title)
                            continue
                        else:
                            try:
                                config.collection_1.insert_one(out)
                                product_count += 1
                                total_inserted += 1
                                rank_counter += 1
                                print(f"Inserted to DB ======================> {product_title}")
                            except Exception as e:
                                print(f'DB Insert Error: {e}')

                    if product_count >= 100:
                        break

                if product_count >= 100:
                    break

                page += 1
                querystring["page"] = str(page)

            if total_inserted > 0:
                config.input.update_one({"_id": keyword_id}, {"$set": {"bigbasket_status": "running"}})
                print(f"Keyword '{keyword}' completed")


if __name__ == '__main__':
    get_data()