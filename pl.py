# import config
# import os
# import json
# import hashlib
# from curl_cffi import requests
#
#
# folder = fr'D:\PAGE_SAVE\3619\{config.run_date}\pl'
# if not os.path.exists(folder):
#     print('Folder not exists! Creating...')
#     os.makedirs(folder, exist_ok=True)
# else:
#     print('Folder already exists:', folder)
#
# global brand_name
# global availability
#
#
# def fetch_data():
#     # cookies = {
#     #     '_bb_locSrc': 'default',
#     #     'x-channel': 'web',
#     #     '_bb_cid': '1',
#     #     '_bb_vid': 'MTAxNjc3MTMzMjkwMjU4NDgxNA==',
#     #     '_bb_nhid': '7427',
#     #     '_bb_dsid': '7427',
#     #     '_bb_dsevid': '7427',
#     #     '_bb_bhid': '',
#     #     '_bb_loid': '',
#     #     'csrftoken': 'WJP6eYx1y5qYv2XdzjmNGayhhqX5t1ufdPWWW1mmNwSpSSvfxkqJL1sqDRMGW1O3',
#     #     'isintegratedsa': 'true',
#     #     'jentrycontextid': '10',
#     #     'xentrycontextid': '10',
#     #     'xentrycontext': 'bbnow',
#     #     '_bb_bb2.0': '1',
#     #     '_is_tobacco_enabled': '1',
#     #     '_is_bb1.0_supported': '0',
#     #     'is_integrated_sa': '1',
#     #     'is_subscribe_sa': '0',
#     #     'bb2_enabled': 'true',
#     #     '_gcl_au': '1.1.1371246423.1764671519',
#     #     'ufi': '1',
#     #     'bigbasket.com': '487899fc-dd49-4a2e-a28f-d4edb52c72a8',
#     #     'jarvis-id': 'ae3f9882-d1e9-4815-b343-bd207e4049d5',
#     #     '_fbp': 'fb.1.1764671519860.783696408437353883',
#     #     'adb': '0',
#     #     '_bb_lat_long': '"MTIuOTEzNDgzNXw3Ny42NzA0NTM5OTk5OTk5OQ=="',
#     #     '_bb_aid': '"MzAxNDI3NDQwMQ=="',
#     #     'is_global': '0',
#     #     '_bb_addressinfo': 'MTIuOTEzNDgzNXw3Ny42NzA0NTM5OTk5OTk5OXxBbWJhbGlwdXJhfDU2MDEwMnxCZW5nYWx1cnV8MXxmYWxzZXx0cnVlfHRydWV8QmlnYmFza2V0ZWVy',
#     #     '_bb_pin_code': '560102',
#     #     '_bb_sa_ids': '14071,24554',
#     #     '_bb_cda_sa_info': 'djIuY2RhX3NhLjEwLjE0MDcxLDI0NTU0',
#     #     'csurftoken': 'kOpbnA.MTAxNjc3MTMzMjkwMjU4NDgxNA==.1765344987937.J1EAkxZZo50I/xMqAPXKRodd0y/ZHV7MTgxzeuhiYX0=',
#     #     '_ga': 'GA1.2.2098795056.1764671520',
#     #     '_gid': 'GA1.2.964664504.1765344993',
#     #     '_gat_UA-27455376-1': '1',
#     #     'ts': '2025-12-10%2011:06:49.608',
#     #     '_ga_FRRYG5VKHX': 'GS2.1.s1765344992$o16$g1$t1765345024$j28$l0$h0',
#     # }
#
#     headers = {
#         'accept': '*/*',
#         'accept-language': 'en-US,en;q=0.9',
#         'common-client-static-version': '101',
#         'content-type': 'application/json',
#         'osmos-enabled': 'true',
#         'priority': 'u=1, i',
#         'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
#         'sec-ch-ua-mobile': '?0',
#         'sec-ch-ua-platform': '"Windows"',
#         'sec-fetch-dest': 'empty',
#         'sec-fetch-mode': 'cors',
#         'sec-fetch-site': 'same-origin',
#         'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
#         'x-channel': 'BB-WEB',
#         'x-entry-context': 'bbnow',
#         'x-entry-context-id': '10',
#         'x-integrated-fc-door-visible': 'false',
#         'x-tracker': '33666ae7-32ec-4e21-8bbf-29a0a9f7c8b2',
#         'cookie': '_bb_locSrc=default; x-channel=web; _bb_cid=1; _bb_vid=MTAxNjc3MTMzMjkwMjU4NDgxNA==; _bb_nhid=7427; _bb_dsid=7427; _bb_dsevid=7427; _bb_bhid=; _bb_loid=; csrftoken=WJP6eYx1y5qYv2XdzjmNGayhhqX5t1ufdPWWW1mmNwSpSSvfxkqJL1sqDRMGW1O3; _bb_bb2.0=1; _is_bb1.0_supported=0; is_subscribe_sa=0; bb2_enabled=true; _gcl_au=1.1.1371246423.1764671519; ufi=1; bigbasket.com=487899fc-dd49-4a2e-a28f-d4edb52c72a8; jarvis-id=ae3f9882-d1e9-4815-b343-bd207e4049d5; _fbp=fb.1.1764671519860.783696408437353883; adb=0; is_global=0; _gid=GA1.2.964664504.1765344993; _bb_lat_long=MTIuOTc2NTk0NHw3Ny41OTkyNzA4; _bb_aid="MzAwNDkxOTI2MA=="; _bb_addressinfo=MTIuOTc2NTk0NHw3Ny41OTkyNzA4fFNoYW50aGFsYSBOYWdhcnw1NjAwMDF8QmVuZ2FsdXJ1fDF8ZmFsc2V8dHJ1ZXx0cnVlfEJpZ2Jhc2tldGVlcg==; _bb_pin_code=560001; is_integrated_sa=1; isintegratedsa=true; jentrycontextid=10; xentrycontextid=10; xentrycontext=bbnow; _bb_sa_ids=24553,27069; _is_tobacco_enabled=1; _bb_cda_sa_info=djIuY2RhX3NhLjEwLjI0NTUzLDI3MDY5; bm_ss=ab8e18ef4e; csurftoken=v13L8Q.MTAxNjc3MTMzMjkwMjU4NDgxNA==.1765434301963.33laYjWuqiGHq1KqY+L7gH6s+J1TkztUl7EPIrfypuc=; bm_so=57AFA30639C1E5C9E4390E4AC573B38CD876071F438C3EB59277EED13BD15F85~YAAQn/Q3F+q7LLWaAQAAMq4cDAVMfLEEL1mCNm7t5q1mWCxO9OqU+jYs/YxOj9Krk1lWY3raPQc+l3Kb9cH7vhgNoQFhdmVsCMVVf2bXEH74rkADrDJCPP4hsNIxcW/rKEPCQBPCidX9tTVYHTCXKJZnGDe8PqrHogkg7suat75jEivpPwEVLeBH+YNb0qH4Ed5dB+AK/S23aiiCM9xjme3roTZgJ7Hun5AadmLsLTpa9Kcb8OLFMra7aCmRA5rKRn6L5WeBRqQFGoBCK9k9R3WF+1MMUi1SeUBt3/MARRmeCNi4wFaEATLD+5e2MGHcEuhiN1CO6Cy7HVNV10bCA3LDE7wXLoKQKhpw3e59m82hNwhYU9Sp0mja/HIkpGqCr+ldrKWHHZRHmYj89Tl75St6QYeikN3jCsUnyb9TWyd0wSXiiq/NGv3tsWhj2Sc8jKJhpU9VyQq+MBIxzQow+Ac=; _gat_UA-27455376-1=1; bm_lso=57AFA30639C1E5C9E4390E4AC573B38CD876071F438C3EB59277EED13BD15F85~YAAQn/Q3F+q7LLWaAQAAMq4cDAVMfLEEL1mCNm7t5q1mWCxO9OqU+jYs/YxOj9Krk1lWY3raPQc+l3Kb9cH7vhgNoQFhdmVsCMVVf2bXEH74rkADrDJCPP4hsNIxcW/rKEPCQBPCidX9tTVYHTCXKJZnGDe8PqrHogkg7suat75jEivpPwEVLeBH+YNb0qH4Ed5dB+AK/S23aiiCM9xjme3roTZgJ7Hun5AadmLsLTpa9Kcb8OLFMra7aCmRA5rKRn6L5WeBRqQFGoBCK9k9R3WF+1MMUi1SeUBt3/MARRmeCNi4wFaEATLD+5e2MGHcEuhiN1CO6Cy7HVNV10bCA3LDE7wXLoKQKhpw3e59m82hNwhYU9Sp0mja/HIkpGqCr+ldrKWHHZRHmYj89Tl75St6QYeikN3jCsUnyb9TWyd0wSXiiq/NGv3tsWhj2Sc8jKJhpU9VyQq+MBIxzQow+Ac=^1765434768596; _ga=GA1.2.2098795056.1764671520; ts=2025-12-11%2012:02:53.673; bm_s=YAAQn/Q3F7XGLLWaAQAA/dscDARbHsVrORfHlz8nw3KEEKmgZ8YxDMq7x33gMveTOx/hBPOrno83ZYkqWWuNdfNMLRKQAMjpl4qchMme4hWUymCf10di1TMRC3tRp/RikvLsYnVRG9UQeR65pmSlIwHCFZcr9MOMtySXdpX+I3aXGMFTWhggIQyvWKirOx+qeT4vlv7AhUZF7tC712zNb1TzfZZx5ISGhouZg2EO+SxXWhbdxSMH9iJsbGinLQH8FG7Ohkv/aFwNB9QYcb7kVvnW/oHaBGwKzlygv7xPp1L5Osfy/BpsHeQNg3NYLl8Gp3Kh5HVUEQjpkJd+hKBKyCFyJPxLsOzs2LNR4Fiu6+Yq5ZsG1kTPqY+OEz4Uhzbu+OK4aXJYSwyLXQ1NJN32gXSPb0+PLx+/47BHvrO0S7rqvdRAi8A77dY7KYn6FujqkEfI3zqL/CwGDeAec0+UZnFi+eaA1wpumAv3tTbqFH/mOD9liRQMmv8vxNRUN+fb/kOS0ksoxmiOrQeJZbqd+ApZmsZh2yFNQjKcpoJpQZNatOyC6YjQlcLdasTU2Doe7DuXKCA0XQ==; _ga_FRRYG5VKHX=GS2.1.s1765428796$o23$g1$t1765434776$j48$l0$h0',
#     }
#
#
#
#     session = requests.Session()
#     session.headers.update(headers)
#     # session.cookies.update(cookies)
#
#     pending_keywords = list(config.input.find({"bigbasket_status": "pending"}))
#     # pending_keywords = list(config.input.find({"keyword": "noodles packet"}))
#     if not pending_keywords:
#         print("No pending keywords found.")
#         return
#
#     for kw_entry in pending_keywords:
#         keyword = kw_entry['keyword']
#         keyword_id = kw_entry['_id']
#         zipcode = kw_entry['zipcode']
#         input_hashid = kw_entry['hashid']
#         api_key = kw_entry['api_key']
#
#         session.cookies['_bb_pin_code'] = str(zipcode)
#
#         product_count = 0
#         total_inserted = 0
#         page = 1
#         params = {
#             'type': 'ps',
#             'slug': f'{keyword}',
#             'page': f'{page}',
#             'bucket_id': '28',
#         }
#         while True:
#             params['slug'] = keyword
#             params['page'] = str(page)
#
#             # url = f"https://www.bigbasket.com/listing-svc/v2/products?type=ps&slug={keyword}&page={page}&bucket_id=28"
#             url = f"https://www.bigbasket.com/listing-svc/v2/products"
#
#             cache_key = f"{keyword}-{zipcode}-{page}"
#             hash_utf8 = cache_key.encode("utf8")
#             r_url_hash_id = str(int(hashlib.md5(hash_utf8).hexdigest(), 16) % (10 ** 10))
#             file_path = os.path.join(folder, f"{r_url_hash_id}.html")
#
#             if os.path.exists(file_path):
#                 print(f"Page already saved: {file_path}")
#                 with open(file_path, "r", encoding="utf-8") as f:
#                     content = f.read()
#             else:
#                 print(f"Fetching page from URL: {url}")
#                 response = requests.get(url, params=params, headers=headers, impersonate="chrome101")
#                 print(f"Status code: {response.status_code}")
#
#                 if response.status_code == 200:
#                     content = response.text
#                     with open(file_path, "w", encoding="utf-8") as f:
#                         f.write(content)
#                 else:
#                     print('Exiting - No more pages or page blocked.')
#                     break
#
#             json_data = json.loads(content)
#             main_data = json_data.get('tabs',[])
#
#             for i in main_data:
#                 for prd_data in i.get('product_info', {}).get('products', []):
#
#                     if product_count >= 100:
#                         break
#
#                     id = prd_data.get('id')
#                     product_title = prd_data.get('desc')
#                     weight = prd_data.get('w')
#                     product_url = prd_data.get('absolute_url')
#                     sku_id = prd_data.get('requested_sku_id')
#
#
#                     image_urls = [img.get('s', '') for img in prd_data.get('images', []) if 's' in img]
#                     all_image_url = "  ,  ".join(image_urls)
#                     first_image_url = image_urls[0] if image_urls else ""
#
#
#                     brand_name = ""
#                     brand_data = prd_data.get('brand')
#                     if isinstance(brand_data, list):
#                         for brand in brand_data:
#                             brand_name = brand.get('name', "")
#                             break
#                     elif isinstance(brand_data, dict):
#                         brand_name = brand_data.get('name', "")
#                     else:
#                         brand_name = brand_data
#
#
#                     availability = "Out of Stock"
#                     availability_data = prd_data.get('availability')
#                     if isinstance(availability_data, list):
#                         for available in availability_data:
#                             stock = available.get('avail_status', "")
#                             if stock == "001":
#                                 availability = "Available"
#                                 break
#                     elif isinstance(availability_data, dict):
#                         stock = availability_data.get('avail_status', "")
#                         if stock == "001":
#                             availability = "Available"
#                     else:  # string case
#                         if availability_data == "001":
#                             availability = "Available"
#
#
#                     mrp = ""
#                     discount_in_per = ""
#                     selling_price = ""
#                     discount_data = prd_data.get('pricing', {}).get('discount')
#                     if isinstance(discount_data, list):
#                         for discount in discount_data:
#                             if isinstance(discount, dict):
#                                 mrp = discount.get('mrp', "")
#                                 discount_in_per = discount.get('d_text', "")
#                                 selling_price = discount.get('subscription_price', "")
#                                 break
#                     elif isinstance(discount_data, dict):
#                         mrp = discount_data.get('mrp', "")
#                         discount_in_per = discount_data.get('d_text', "")
#                         selling_price = discount_data.get('subscription_price', "")
#                     else:
#                         # discount_data is a string — no mrp/selling_price available
#                         discount_in_per = str(discount_data)
#
#
#                     raw_key = f"{id}-{keyword}-{zipcode}"
#                     hash_id = hashlib.md5(raw_key.encode()).hexdigest()[:12]
#
#
#                     out = {}
#                     out['input_hashid'] = input_hashid
#                     out['input_zipcode'] = zipcode
#                     out['keyword'] = keyword
#                     out['api_key'] = api_key
#                     out['hashid'] = hash_id
#                     out["id"] = id
#                     out["product_title"] = product_title
#                     out["brand"] = brand_name
#                     out["main_image"] = first_image_url
#                     out["Pincode"] = zipcode
#                     out["availability"] = availability
#                     out["msrp"] = mrp
#                     out["thumbnail_image_url"] = first_image_url
#                     out["detail_page_images"] = all_image_url
#                     out["Platform url of the SKU"] = 'https://www.bigbasket.com' + product_url
#                     out["sell_price"] = selling_price
#                     out['images'] = len(image_urls)
#                     out['weight'] = weight
#                     out['sku_id'] = sku_id
#                     out['discount_in_per'] = discount_in_per
#                     out['pl_page_save_path'] = file_path
#                     out['status'] = 'pending'
#
#                     if config.collection_1.find_one({"hash_id": hash_id}):
#                         print("Duplicate entry skipped!", product_title)
#                         continue
#                     else:
#                         try:
#                             config.collection_1.insert_one(out)
#                             product_count += 1
#                             total_inserted += 1
#                             print(f"Inserted to DB: {product_title}")
#                         except Exception as e:
#                             print(f'DB Insert Error: {e}')
#
#                 if product_count >= 100:
#                     break
#
#             if product_count >= 100:
#                 break
#
#             page += 1
#
#         if total_inserted > 0:
#             config.input.update_one({"_id": keyword_id}, {"$set": {"bigbasket_status": "running"}})
#             print(f"Keyword '{keyword}' status updated to running")
#
#
# if __name__ == '__main__':
#     fetch_data()