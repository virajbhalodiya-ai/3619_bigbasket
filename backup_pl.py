# import config
# import os
# import json
# import hashlib
# from curl_cffi import requests
#
# folder = r'D:\Harsh Sir\Page_save\3619\pl'
# if not os.path.exists(folder):
#     print('Folder not exists! Creating...')
#     os.mkdir(folder)
#
# global brand_name
# global availability
#
#
# def fetch_data():
#     cookies = {
#         '_bb_locSrc': 'default',
#         'x-channel': 'web',
#         '_bb_cid': '1',
#         '_bb_vid': 'MTAxNjc3MTMzMjkwMjU4NDgxNA==',
#         '_bb_nhid': '7427',
#         '_bb_dsid': '7427',
#         '_bb_dsevid': '7427',
#         '_bb_bhid': '',
#         '_bb_loid': '',
#         'csrftoken': 'WJP6eYx1y5qYv2XdzjmNGayhhqX5t1ufdPWWW1mmNwSpSSvfxkqJL1sqDRMGW1O3',
#         'isintegratedsa': 'true',
#         'jentrycontextid': '10',
#         'xentrycontextid': '10',
#         'xentrycontext': 'bbnow',
#         '_bb_bb2.0': '1',
#         '_is_tobacco_enabled': '1',
#         '_is_bb1.0_supported': '0',
#         'is_integrated_sa': '1',
#         'is_subscribe_sa': '0',
#         'bb2_enabled': 'true',
#         '_gcl_au': '1.1.1371246423.1764671519',
#         'ufi': '1',
#         'bigbasket.com': '487899fc-dd49-4a2e-a28f-d4edb52c72a8',
#         'jarvis-id': 'ae3f9882-d1e9-4815-b343-bd207e4049d5',
#         '_fbp': 'fb.1.1764671519860.783696408437353883',
#         '_gid': 'GA1.2.416728496.1764671520',
#         'adb': '0',
#         '_bb_lat_long': '"MTIuOTEzNDgzNXw3Ny42NzA0NTM5OTk5OTk5OQ=="',
#         '_bb_aid': '"MzAxNDI3NDQwMQ=="',
#         'is_global': '0',
#         '_bb_addressinfo': 'MTIuOTEzNDgzNXw3Ny42NzA0NTM5OTk5OTk5OXxBbWJhbGlwdXJhfDU2MDEwMnxCZW5nYWx1cnV8MXxmYWxzZXx0cnVlfHRydWV8QmlnYmFza2V0ZWVy',
#         '_bb_pin_code': '560102',
#         '_bb_sa_ids': '14071,24554',
#         '_bb_cda_sa_info': 'djIuY2RhX3NhLjEwLjE0MDcxLDI0NTU0',
#         'csurftoken': 'fkMwog.MTAxNjc3MTMzMjkwMjU4NDgxNA==.1764676561533.ECbV9TwFfBhHNWzXanYY1ohL/Ha6WlNizHsLk+EgCzs=',
#         '_ga': 'GA1.2.2098795056.1764671520',
#         '_gat_UA-27455376-1': '1',
#         'ts': '2025-12-02%2017:26:09.959',
#         '_ga_FRRYG5VKHX': 'GS2.1.s1764676567$o2$g1$t1764676578$j49$l0$h0',
#     }
#
#     headers = {
#         'accept': '*/*',
#         'accept-language': 'en-US,en;q=0.9',
#         'common-client-static-version': '101',
#         'content-type': 'application/json',
#         'osmos-enabled': 'true',
#         'priority': 'u=1, i',
#         'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
#         'x-channel': 'BB-WEB',
#         'x-entry-context': 'bbnow',
#         'x-entry-context-id': '10',
#         'x-integrated-fc-door-visible': 'false',
#         'x-tracker': '85c876b6-64b6-4152-8a43-8bc3fffd2dfc',
#         # 'cookie': '_bb_locSrc=default; x-channel=web; _bb_cid=1; _bb_vid=MTAxNjc3MTMzMjkwMjU4NDgxNA==; _bb_nhid=7427; _bb_dsid=7427; _bb_dsevid=7427; _bb_bhid=; _bb_loid=; csrftoken=WJP6eYx1y5qYv2XdzjmNGayhhqX5t1ufdPWWW1mmNwSpSSvfxkqJL1sqDRMGW1O3; isintegratedsa=true; jentrycontextid=10; xentrycontextid=10; xentrycontext=bbnow; _bb_bb2.0=1; _is_tobacco_enabled=1; _is_bb1.0_supported=0; is_integrated_sa=1; is_subscribe_sa=0; bb2_enabled=true; _gcl_au=1.1.1371246423.1764671519; ufi=1; bigbasket.com=487899fc-dd49-4a2e-a28f-d4edb52c72a8; jarvis-id=ae3f9882-d1e9-4815-b343-bd207e4049d5; _fbp=fb.1.1764671519860.783696408437353883; _gid=GA1.2.416728496.1764671520; adb=0; _bb_lat_long="MTIuOTEzNDgzNXw3Ny42NzA0NTM5OTk5OTk5OQ=="; _bb_aid="MzAxNDI3NDQwMQ=="; is_global=0; _bb_addressinfo=MTIuOTEzNDgzNXw3Ny42NzA0NTM5OTk5OTk5OXxBbWJhbGlwdXJhfDU2MDEwMnxCZW5nYWx1cnV8MXxmYWxzZXx0cnVlfHRydWV8QmlnYmFza2V0ZWVy; _bb_pin_code=560102; _bb_sa_ids=14071,24554; _bb_cda_sa_info=djIuY2RhX3NhLjEwLjE0MDcxLDI0NTU0; csurftoken=fkMwog.MTAxNjc3MTMzMjkwMjU4NDgxNA==.1764676561533.ECbV9TwFfBhHNWzXanYY1ohL/Ha6WlNizHsLk+EgCzs=; _ga=GA1.2.2098795056.1764671520; _gat_UA-27455376-1=1; ts=2025-12-02%2017:26:09.959; _ga_FRRYG5VKHX=GS2.1.s1764676567$o2$g1$t1764676578$j49$l0$h0',
#     }
#
#     params = {
#         'type': 'ps',
#         'slug': 'noodles',
#         'page': '1',
#         'bucket_id': '28',
#     }
#
#     session = requests.Session()
#     session.headers.update(headers)
#     session.cookies.update(cookies)
#
#     pincodes = ['562125', '560114', '560111']
#     keywords = ['noodles', 'ramen', 'chow mein', 'pasta varieties', 'ramen noodles', 'noodles for ramen',
#                 'ramen near me', 'korean noodles',
#                 'ramen food near me', 'shirataki noodles', 'shirataki rice', 'fettuccine', 'rice noodles', 'ramen bowl',
#                 'buldak noodles',
#                 'udon noodles', 'pad thai noodles', 'korean ramen', 'millet noodles', 'chicken noodles', 'soba noodles',
#                 'top ramen',
#                 'glass noodles', 'vegetable noodles', 'jajangmyeon', 'cellophane noodles', 'vegan ramen',
#                 'lasagna sheets', 'vegetarian ramen',
#                 'japchae', 'udon', 'chinese noodles', 'singapore noodles', 'chilli garlic noodles',
#                 'singapore style noodles', 'egg noodles',
#                 'spicy noodles', 'ramyeon', 'miso ramen', 'noodles and eggs', 'rice noodle roll', 'veg chowmein',
#                 'chow mein noodles',
#                 'rice vermicelli', 'kimchi ramen', 'korean ramen noodles', 'wheat noodles', 'flat noodles',
#                 'ramen shop near me',
#                 'kimchi ramen noodles', 'maggi masala', 'noodles packet', 'indo mie', 'atta maggi', 'packet noodles',
#                 'yippee maggi',
#                 'ramen packet', 'knorr soupy noodles', 'ramen noodles packet', 'atta noodles', 'korean maggi',
#                 'maggi packet', 'cheese maggi',
#                 'instant noodles', 'top ramen noodles', 'instant ramen noodles', 'maggi cup noodles',
#                 'maggi atta noodles', 'korean noodles packet',
#                 'mi goreng', 'yippee noodles price', 'knorr noodles', 'oats maggi', 'top ramen curry noodles',
#                 'spicy maggi', 'veg atta maggi',
#                 'instant pasta', 'korean cup noodles', 'maggi chicken noodles', 'maggi ramen', 'maggi packet price',
#                 'ramen maggi', 'instant ramen',
#                 'buldak cup noodles', 'maggi noodles price', 'korean noodles veg', 'atta maggi price',
#                 'maggi special masala', 'maggi masala powder',
#                 'noodles maggi', 'maggi masala noodles', 'instant ramen bowl', 'noodles packet price',
#                 'korean instant noodles', 'maggi products',
#                 'chinese noodles packet', 'maggi price 10 rs', 'mi goreng noodles', 'maggi cup',
#                 'maggi 2 minute noodles']
#
#     for pincode in pincodes:
#         session.cookies.update({'_bb_pin_code': pincode})
#
#         for keyword in keywords:
#             page = 1
#             while True:
#                 params['slug'] = keyword
#                 params['page'] = str(page)
#
#                 url = f"https://www.bigbasket.com/listing-svc/v2/products?type=ps&slug={keyword}&page={page}&bucket_id=28"
#
#                 hash_utf8 = url.encode('utf8')
#                 r_url_hash_id = str(int(hashlib.md5(hash_utf8).hexdigest(), 16) % (10 ** 10))
#                 file_path = os.path.join(folder, f"{r_url_hash_id}.html")
#
#                 if os.path.exists(file_path):
#                     print(f"Page already saved: {file_path}")
#                     with open(file_path, "r", encoding="utf-8") as f:
#                         content = f.read()
#                 else:
#                     print(f"Fetching page from URL: {url}")
#                     response = session.get(url, params=params)
#                     print(f"Status code: {response.status_code}")
#
#                     if response.status_code == 200:
#                         content = response.text
#                         with open(file_path, "w", encoding="utf-8") as f:
#                             f.write(content)
#                     else:
#                         print('Exiting - No more pages or page blocked.')
#                         break
#
#                 json_data = json.loads(content)
#                 main_data = json_data['tabs']
#
#                 for i in main_data['product_info']['products']:
#                     for prd_data in i:
#                         id = prd_data['id']
#                         product_title = prd_data['desc']
#                         weight = prd_data['w']
#                         product_url = prd_data['absolute_url']
#                         sku_id = prd_data['requested_sku_id']
#
#                         image_urls = []
#                         for img in prd_data.get('images', []):
#                             for img_url in img:
#                                 if 's' in img_url:
#                                     image_urls.append(img_url['s'])
#                         all_image_url = ",".join(image_urls)
#
#                         first_image_url = next(
#                             (img_url['s'] for img in prd_data.get('images', []) for img_url in img if 's' in img_url),
#                             "")
#
#                         for brand in prd_data['brand']:
#                             brand_name = brand['name']
#
#                         for available in prd_data['availability']:
#                             stock = available['avail_status']
#                             if stock == "001":
#                                 availability = "Available"
#                             else:
#                                 availability = "Out of Stock"
#
#                         for discount in prd_data['pricing']['discount']:
#                             mrp = discount['mrp']
#                             discount_in_per = discount['d_text']
#                             selling_price = discount['subscription_price']
#
#                             raw_key = f"{id}-{pincode}-{keyword}"
#                             hash_id = hashlib.md5(raw_key.encode()).hexdigest()
#
#                             out = {}
#                             out['hash_id'] = hash_id
#                             out['keyword'] = keyword
#                             out["id"] = id
#                             out["product_title"] = product_title
#                             out["brand"] = brand_name
#                             out["main_image"] = first_image_url
#                             out["Pincode"] = pincode
#                             out["availability"] = availability
#                             out["msrp"] = mrp
#                             out["thumbnail_image_url"] = first_image_url
#                             out["detail_page_images"] = all_image_url
#                             out["Platform url of the SKU"] = product_url
#                             out["sell_price"] = selling_price
#                             out['weight'] = weight
#                             out['sku_id'] = sku_id
#                             out['discount_in_per'] = discount_in_per
#
#                             if config.collection_1.find_one({"hash_id": hash_id}):
#                                 print("Duplicate entry skipped!", product_title)
#                                 continue
#                             else:
#                                 try:
#                                     config.collection_1.insert_one(out)
#                                     print(f"Inserted to DB: {product_title}")
#                                 except Exception as e:
#                                     print(f'DB Insert Error: {e}')
#
#
# if __name__ == '__main__':
#     fetch_data()






import config
import os
import json
import hashlib
from curl_cffi import requests


folder = r'D:\Harsh Sir\Page_save\3619\pl'
if not os.path.exists(folder):
    print('Folder not exists! Creating...')
    os.mkdir(folder)

global brand_name
global availability


def fetch_data():
    cookies = {
        '_bb_locSrc': 'default',
        'x-channel': 'web',
        '_bb_cid': '1',
        '_bb_vid': 'MTAxNjc3MTMzMjkwMjU4NDgxNA==',
        '_bb_nhid': '7427',
        '_bb_dsid': '7427',
        '_bb_dsevid': '7427',
        '_bb_bhid': '',
        '_bb_loid': '',
        'csrftoken': 'WJP6eYx1y5qYv2XdzjmNGayhhqX5t1ufdPWWW1mmNwSpSSvfxkqJL1sqDRMGW1O3',
        'isintegratedsa': 'true',
        'jentrycontextid': '10',
        'xentrycontextid': '10',
        'xentrycontext': 'bbnow',
        '_bb_bb2.0': '1',
        '_is_tobacco_enabled': '1',
        '_is_bb1.0_supported': '0',
        'is_integrated_sa': '1',
        'is_subscribe_sa': '0',
        'bb2_enabled': 'true',
        '_gcl_au': '1.1.1371246423.1764671519',
        'ufi': '1',
        'bigbasket.com': '487899fc-dd49-4a2e-a28f-d4edb52c72a8',
        'jarvis-id': 'ae3f9882-d1e9-4815-b343-bd207e4049d5',
        '_fbp': 'fb.1.1764671519860.783696408437353883',
        'adb': '0',
        '_bb_lat_long': '"MTIuOTEzNDgzNXw3Ny42NzA0NTM5OTk5OTk5OQ=="',
        '_bb_aid': '"MzAxNDI3NDQwMQ=="',
        'is_global': '0',
        '_bb_addressinfo': 'MTIuOTEzNDgzNXw3Ny42NzA0NTM5OTk5OTk5OXxBbWJhbGlwdXJhfDU2MDEwMnxCZW5nYWx1cnV8MXxmYWxzZXx0cnVlfHRydWV8QmlnYmFza2V0ZWVy',
        '_bb_pin_code': '560102',
        '_bb_sa_ids': '14071,24554',
        '_bb_cda_sa_info': 'djIuY2RhX3NhLjEwLjE0MDcxLDI0NTU0',
        'csurftoken': 'kOpbnA.MTAxNjc3MTMzMjkwMjU4NDgxNA==.1765344987937.J1EAkxZZo50I/xMqAPXKRodd0y/ZHV7MTgxzeuhiYX0=',
        '_ga': 'GA1.2.2098795056.1764671520',
        '_gid': 'GA1.2.964664504.1765344993',
        '_gat_UA-27455376-1': '1',
        'ts': '2025-12-10%2011:06:49.608',
        '_ga_FRRYG5VKHX': 'GS2.1.s1765344992$o16$g1$t1765345024$j28$l0$h0',
    }

    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9',
        'common-client-static-version': '101',
        'content-type': 'application/json',
        'osmos-enabled': 'true',
        'priority': 'u=1, i',
        'sec-ch-ua': '"Chromium";v="142", "Google Chrome";v="142", "Not_A Brand";v="99"',
        'sec-ch-ua-mobile': '?0',
        'sec-ch-ua-platform': '"Windows"',
        'sec-fetch-dest': 'empty',
        'sec-fetch-mode': 'cors',
        'sec-fetch-site': 'same-origin',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/142.0.0.0 Safari/537.36',
        'x-channel': 'BB-WEB',
        'x-entry-context': 'bbnow',
        'x-entry-context-id': '10',
        'x-integrated-fc-door-visible': 'false',
        'x-tracker': '7027e429-5e99-44ff-a2cb-f743bcc20fee',
        # 'cookie': '_bb_locSrc=default; x-channel=web; _bb_cid=1; _bb_vid=MTAxNjc3MTMzMjkwMjU4NDgxNA==; _bb_nhid=7427; _bb_dsid=7427; _bb_dsevid=7427; _bb_bhid=; _bb_loid=; csrftoken=WJP6eYx1y5qYv2XdzjmNGayhhqX5t1ufdPWWW1mmNwSpSSvfxkqJL1sqDRMGW1O3; isintegratedsa=true; jentrycontextid=10; xentrycontextid=10; xentrycontext=bbnow; _bb_bb2.0=1; _is_tobacco_enabled=1; _is_bb1.0_supported=0; is_integrated_sa=1; is_subscribe_sa=0; bb2_enabled=true; _gcl_au=1.1.1371246423.1764671519; ufi=1; bigbasket.com=487899fc-dd49-4a2e-a28f-d4edb52c72a8; jarvis-id=ae3f9882-d1e9-4815-b343-bd207e4049d5; _fbp=fb.1.1764671519860.783696408437353883; adb=0; _bb_lat_long="MTIuOTEzNDgzNXw3Ny42NzA0NTM5OTk5OTk5OQ=="; _bb_aid="MzAxNDI3NDQwMQ=="; is_global=0; _bb_addressinfo=MTIuOTEzNDgzNXw3Ny42NzA0NTM5OTk5OTk5OXxBbWJhbGlwdXJhfDU2MDEwMnxCZW5nYWx1cnV8MXxmYWxzZXx0cnVlfHRydWV8QmlnYmFza2V0ZWVy; _bb_pin_code=560102; _bb_sa_ids=14071,24554; _bb_cda_sa_info=djIuY2RhX3NhLjEwLjE0MDcxLDI0NTU0; csurftoken=kOpbnA.MTAxNjc3MTMzMjkwMjU4NDgxNA==.1765344987937.J1EAkxZZo50I/xMqAPXKRodd0y/ZHV7MTgxzeuhiYX0=; _ga=GA1.2.2098795056.1764671520; _gid=GA1.2.964664504.1765344993; _gat_UA-27455376-1=1; ts=2025-12-10%2011:06:49.608; _ga_FRRYG5VKHX=GS2.1.s1765344992$o16$g1$t1765345024$j28$l0$h0',
    }

    params = {
        'type': 'ps',
        'slug': 'maggi masala',
        'page': '1',
        'bucket_id': '28',
    }

    session = requests.Session()
    session.headers.update(headers)
    session.cookies.update(cookies)

    pending_keywords = list(config.input.find({"status": "pending"}))
    if not pending_keywords:
        print("No pending keywords found.")
        return

    for kw_entry in pending_keywords:
        keyword = kw_entry['keyword']
        keyword_id = kw_entry['_id']
        zipcode = kw_entry['zipcode']

        session.cookies['_bb_pin_code'] = str(zipcode)

        product_count = 0
        total_inserted = 0
        page = 1
        while True:
            params['slug'] = keyword
            params['page'] = str(page)

            # url = f"https://www.bigbasket.com/listing-svc/v2/products?type=ps&slug={keyword}&page={page}&bucket_id=28"
            url = f"https://www.bigbasket.com/listing-svc/v2/products"

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
                response = session.get(url, params=params, headers=headers)
                print(f"Status code: {response.status_code}")

                if response.status_code == 200:
                    content = response.text
                    with open(file_path, "w", encoding="utf-8") as f:
                        f.write(content)
                else:
                    print('Exiting - No more pages or page blocked.')
                    break

            json_data = json.loads(content)
            main_data = json_data['tabs']

            for i in main_data:
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
                    else:  # string case
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
                        # discount_data is a string — no mrp/selling_price available
                        discount_in_per = str(discount_data)


                    raw_key = f"{id}-{keyword}-{zipcode}"
                    hash_id = hashlib.md5(raw_key.encode()).hexdigest()[:12]


                    out = {}
                    out['hash_id'] = hash_id
                    out['keyword'] = keyword
                    out["id"] = id
                    out["product_title"] = product_title
                    out["brand"] = brand_name
                    out["main_image"] = first_image_url
                    out["zipcode"] = zipcode
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
                    out['file_path'] = file_path
                    out['status'] = 'pending'

                    if config.collection_1.find_one({"hash_id": hash_id}):
                        print("Duplicate entry skipped!", product_title)
                        continue
                    else:
                        try:
                            config.collection_1.insert_one(out)
                            product_count += 1
                            total_inserted += 1
                            print(f"Inserted to DB: {product_title}")
                        except Exception as e:
                            print(f'DB Insert Error: {e}')

                if product_count >= 100:
                    break

            if product_count >= 100:
                break

            page += 1

        if total_inserted > 0:
            config.input.update_one({"_id": keyword_id}, {"$set": {"status": "done"}})
            print(f"Keyword '{keyword}' status updated to DONE")


if __name__ == '__main__':
    fetch_data()