# import requests
#
# cookies = {
#     '_bb_locSrc': 'default',
#     'x-channel': 'web',
#     '_bb_cid': '1',
#     '_bb_vid': 'MTAxNjc3MTMzMjkwMjU4NDgxNA==',
#     '_bb_nhid': '7427',
#     '_bb_dsid': '7427',
#     '_bb_dsevid': '7427',
#     '_bb_bhid': '',
#     '_bb_loid': '',
#     'csrftoken': 'WJP6eYx1y5qYv2XdzjmNGayhhqX5t1ufdPWWW1mmNwSpSSvfxkqJL1sqDRMGW1O3',
#     '_bb_bb2.0': '1',
#     '_is_bb1.0_supported': '0',
#     'is_subscribe_sa': '0',
#     'bb2_enabled': 'true',
#     '_gcl_au': '1.1.1371246423.1764671519',
#     'ufi': '1',
#     'bigbasket.com': '487899fc-dd49-4a2e-a28f-d4edb52c72a8',
#     'jarvis-id': 'ae3f9882-d1e9-4815-b343-bd207e4049d5',
#     '_fbp': 'fb.1.1764671519860.783696408437353883',
#     'is_global': '0',
#     '_bb_lat_long': 'MTIuOTc2NTk0NHw3Ny41OTkyNzA4',
#     '_bb_aid': '"MzAwNDkxOTI2MA=="',
#     '_bb_addressinfo': 'MTIuOTc2NTk0NHw3Ny41OTkyNzA4fFNoYW50aGFsYSBOYWdhcnw1NjAwMDF8QmVuZ2FsdXJ1fDF8ZmFsc2V8dHJ1ZXx0cnVlfEJpZ2Jhc2tldGVlcg==',
#     '_bb_pin_code': '560001',
#     'is_integrated_sa': '1',
#     'isintegratedsa': 'true',
#     'jentrycontextid': '10',
#     'xentrycontextid': '10',
#     'xentrycontext': 'bbnow',
#     '_is_tobacco_enabled': '1',
#     '_bb_sa_ids': '24557,27069',
#     '_bb_cda_sa_info': 'djIuY2RhX3NhLjEwLjI0NTU3LDI3MDY5',
#     'adb': '0',
#     'csurftoken': 'nMSNtQ.MTAxNjc3MTMzMjkwMjU4NDgxNA==.1768566813728.LjT/bFBJTsawTxdyzUYw6Ta3IbAhlAFU05YrDBRgQXg=',
#     'bm_ss': 'ab8e18ef4e',
#     '_gid': 'GA1.2.1646954343.1768566815',
#     '_gcl_aw': 'GCL.1768566852.CjwKCAiA4KfLBhB0EiwAUY7GAYE8nso43uUOb3zsWAVY5Y43OsFfSe027OMouApXTPPiuX4LybsYtBoCgu0QAvD_BwE',
#     '_gcl_gs': '2.1.k1$i1768566849$u160754478',
#     '_gac_UA-27455376-1': '1.1768566852.CjwKCAiA4KfLBhB0EiwAUY7GAYE8nso43uUOb3zsWAVY5Y43OsFfSe027OMouApXTPPiuX4LybsYtBoCgu0QAvD_BwE',
#     '_ga_FRRYG5VKHX': 'GS2.1.s1768566815$o13$g1$t1768567273$j54$l0$h0',
#     '_ga': 'GA1.2.54261959.1765449151',
#     'ts': '2026-01-16%2018:19:38.677',
#     'bm_so': '916AA3CB9B5255D612CE44277802CAB85DABDA58CE46E021260C3B2ED912F3FD~YAAQlvnaF9NHusGbAQAArYPcxgZOk56pSJ3P5rerya2KwYx0e7ogsDrImYZryA/WTdVuCy4+Q3/0aR6qySLxVEhcf6Bm3CEb/WaJiI7nSLF/UaEF5sGr7d6iHRHbCpetEhdxGM2j6tMEcvO83Z/C0d9noOOVeL19SDVg6VYkO8OaRyOQfYw2tw1B5L1rf2V75vNR4KecdxeSflXAdvvX9nj1bhcsOcSMR4GtFDgo6FbeVkylA4UyJ4G0Av1kThQLB7ADcjWwp1AUCkSr2ELSx63/PCDKAUrWNlWO1aF7TgkWOpVcNi5cJJ3VgPpYi7NQjWvJ+0Kr6OJlaFBhRFI588/o5TjjgghUWTXeXzcBelLUL+HKjQh84oN1oK9txO7Il0ap3CT9yn18cCkqsI55LWFEjZ6zhZ4o1K/m1iEMOA480zsSeYEWRUgMCzJj6fhRX/iulco5OvJre0ao6yl3ObQ=',
#     'bm_lso': '916AA3CB9B5255D612CE44277802CAB85DABDA58CE46E021260C3B2ED912F3FD~YAAQlvnaF9NHusGbAQAArYPcxgZOk56pSJ3P5rerya2KwYx0e7ogsDrImYZryA/WTdVuCy4+Q3/0aR6qySLxVEhcf6Bm3CEb/WaJiI7nSLF/UaEF5sGr7d6iHRHbCpetEhdxGM2j6tMEcvO83Z/C0d9noOOVeL19SDVg6VYkO8OaRyOQfYw2tw1B5L1rf2V75vNR4KecdxeSflXAdvvX9nj1bhcsOcSMR4GtFDgo6FbeVkylA4UyJ4G0Av1kThQLB7ADcjWwp1AUCkSr2ELSx63/PCDKAUrWNlWO1aF7TgkWOpVcNi5cJJ3VgPpYi7NQjWvJ+0Kr6OJlaFBhRFI588/o5TjjgghUWTXeXzcBelLUL+HKjQh84oN1oK9txO7Il0ap3CT9yn18cCkqsI55LWFEjZ6zhZ4o1K/m1iEMOA480zsSeYEWRUgMCzJj6fhRX/iulco5OvJre0ao6yl3ObQ=~1768567899420',
#     'bm_s': 'YAAQlvnaFwlMusGbAQAA65HcxgQiIyvpk0hrOBURMuredCEM3JFVvM3hLOtRBolRHN2BjZ38LfiBJq4s9leQqso/t7loC0/ij0JWZCXQ5dS+i+hYOKRljvZsFLvWW7umjPHylDLVFnFq6LF46R3DcwuF4HS1i0kXKHdzKawDGwV5qNxS0+gPaDagrEmr2Sz+CpOBaqpKkNqa+OGHDBlhWVFBUGN9uguHxrQipBj+sPk8iFARw+WiI8Am8kZFg/KFuj6uBIQyC7jWcLoCqH8JmxPFoLoapNkuGuky/TMI2uMG9JCy5MX6iQLp/eqXsGiIe5UPuCo+OqI9SOdLh0lkiD+ARF/FVSxGVYH2xazB0tguZSDS41ddq1lie8HLWA+8Yf2igVf1X/CaRaM8J+9c1MqD+0ZTmwgEncbLfvofzaBapKVD3q7msUnsLd4rS8wFJGusSUgInpWlTVsv/fR8fIVfORImrtnV+IJt/guiHwOvW9ri7sI1AX/mhTSVV9z16MzrX4GvNM9Y7iyp3an4SxoUDbdHA3gFrTaWeAV6xX7syq1hUNIGXapLPnzqZ9CW3B+WOhELkYSJIA==',
# }
#
# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-US,en;q=0.9',
#     'cache-control': 'max-age=0',
#     'priority': 'u=0, i',
#     'sec-ch-ua': '"Google Chrome";v="143", "Chromium";v="143", "Not A(Brand";v="24"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/143.0.0.0 Safari/537.36',
#     # 'cookie': '_bb_locSrc=default; x-channel=web; _bb_cid=1; _bb_vid=MTAxNjc3MTMzMjkwMjU4NDgxNA==; _bb_nhid=7427; _bb_dsid=7427; _bb_dsevid=7427; _bb_bhid=; _bb_loid=; csrftoken=WJP6eYx1y5qYv2XdzjmNGayhhqX5t1ufdPWWW1mmNwSpSSvfxkqJL1sqDRMGW1O3; _bb_bb2.0=1; _is_bb1.0_supported=0; is_subscribe_sa=0; bb2_enabled=true; _gcl_au=1.1.1371246423.1764671519; ufi=1; bigbasket.com=487899fc-dd49-4a2e-a28f-d4edb52c72a8; jarvis-id=ae3f9882-d1e9-4815-b343-bd207e4049d5; _fbp=fb.1.1764671519860.783696408437353883; is_global=0; _bb_lat_long=MTIuOTc2NTk0NHw3Ny41OTkyNzA4; _bb_aid="MzAwNDkxOTI2MA=="; _bb_addressinfo=MTIuOTc2NTk0NHw3Ny41OTkyNzA4fFNoYW50aGFsYSBOYWdhcnw1NjAwMDF8QmVuZ2FsdXJ1fDF8ZmFsc2V8dHJ1ZXx0cnVlfEJpZ2Jhc2tldGVlcg==; _bb_pin_code=560001; is_integrated_sa=1; isintegratedsa=true; jentrycontextid=10; xentrycontextid=10; xentrycontext=bbnow; _is_tobacco_enabled=1; _bb_sa_ids=24557,27069; _bb_cda_sa_info=djIuY2RhX3NhLjEwLjI0NTU3LDI3MDY5; adb=0; csurftoken=nMSNtQ.MTAxNjc3MTMzMjkwMjU4NDgxNA==.1768566813728.LjT/bFBJTsawTxdyzUYw6Ta3IbAhlAFU05YrDBRgQXg=; bm_ss=ab8e18ef4e; _gid=GA1.2.1646954343.1768566815; _gcl_aw=GCL.1768566852.CjwKCAiA4KfLBhB0EiwAUY7GAYE8nso43uUOb3zsWAVY5Y43OsFfSe027OMouApXTPPiuX4LybsYtBoCgu0QAvD_BwE; _gcl_gs=2.1.k1$i1768566849$u160754478; _gac_UA-27455376-1=1.1768566852.CjwKCAiA4KfLBhB0EiwAUY7GAYE8nso43uUOb3zsWAVY5Y43OsFfSe027OMouApXTPPiuX4LybsYtBoCgu0QAvD_BwE; _ga_FRRYG5VKHX=GS2.1.s1768566815$o13$g1$t1768567273$j54$l0$h0; _ga=GA1.2.54261959.1765449151; ts=2026-01-16%2018:19:38.677; bm_so=916AA3CB9B5255D612CE44277802CAB85DABDA58CE46E021260C3B2ED912F3FD~YAAQlvnaF9NHusGbAQAArYPcxgZOk56pSJ3P5rerya2KwYx0e7ogsDrImYZryA/WTdVuCy4+Q3/0aR6qySLxVEhcf6Bm3CEb/WaJiI7nSLF/UaEF5sGr7d6iHRHbCpetEhdxGM2j6tMEcvO83Z/C0d9noOOVeL19SDVg6VYkO8OaRyOQfYw2tw1B5L1rf2V75vNR4KecdxeSflXAdvvX9nj1bhcsOcSMR4GtFDgo6FbeVkylA4UyJ4G0Av1kThQLB7ADcjWwp1AUCkSr2ELSx63/PCDKAUrWNlWO1aF7TgkWOpVcNi5cJJ3VgPpYi7NQjWvJ+0Kr6OJlaFBhRFI588/o5TjjgghUWTXeXzcBelLUL+HKjQh84oN1oK9txO7Il0ap3CT9yn18cCkqsI55LWFEjZ6zhZ4o1K/m1iEMOA480zsSeYEWRUgMCzJj6fhRX/iulco5OvJre0ao6yl3ObQ=; bm_lso=916AA3CB9B5255D612CE44277802CAB85DABDA58CE46E021260C3B2ED912F3FD~YAAQlvnaF9NHusGbAQAArYPcxgZOk56pSJ3P5rerya2KwYx0e7ogsDrImYZryA/WTdVuCy4+Q3/0aR6qySLxVEhcf6Bm3CEb/WaJiI7nSLF/UaEF5sGr7d6iHRHbCpetEhdxGM2j6tMEcvO83Z/C0d9noOOVeL19SDVg6VYkO8OaRyOQfYw2tw1B5L1rf2V75vNR4KecdxeSflXAdvvX9nj1bhcsOcSMR4GtFDgo6FbeVkylA4UyJ4G0Av1kThQLB7ADcjWwp1AUCkSr2ELSx63/PCDKAUrWNlWO1aF7TgkWOpVcNi5cJJ3VgPpYi7NQjWvJ+0Kr6OJlaFBhRFI588/o5TjjgghUWTXeXzcBelLUL+HKjQh84oN1oK9txO7Il0ap3CT9yn18cCkqsI55LWFEjZ6zhZ4o1K/m1iEMOA480zsSeYEWRUgMCzJj6fhRX/iulco5OvJre0ao6yl3ObQ=~1768567899420; bm_s=YAAQlvnaFwlMusGbAQAA65HcxgQiIyvpk0hrOBURMuredCEM3JFVvM3hLOtRBolRHN2BjZ38LfiBJq4s9leQqso/t7loC0/ij0JWZCXQ5dS+i+hYOKRljvZsFLvWW7umjPHylDLVFnFq6LF46R3DcwuF4HS1i0kXKHdzKawDGwV5qNxS0+gPaDagrEmr2Sz+CpOBaqpKkNqa+OGHDBlhWVFBUGN9uguHxrQipBj+sPk8iFARw+WiI8Am8kZFg/KFuj6uBIQyC7jWcLoCqH8JmxPFoLoapNkuGuky/TMI2uMG9JCy5MX6iQLp/eqXsGiIe5UPuCo+OqI9SOdLh0lkiD+ARF/FVSxGVYH2xazB0tguZSDS41ddq1lie8HLWA+8Yf2igVf1X/CaRaM8J+9c1MqD+0ZTmwgEncbLfvofzaBapKVD3q7msUnsLd4rS8wFJGusSUgInpWlTVsv/fR8fIVfORImrtnV+IJt/guiHwOvW9ri7sI1AX/mhTSVV9z16MzrX4GvNM9Y7iyp3an4SxoUDbdHA3gFrTaWeAV6xX7syq1hUNIGXapLPnzqZ9CW3B+WOhELkYSJIA==',
# }
#
# params = {
#     'nc': 'cl-prod-list',
#     't_pos_sec': '1',
#     't_pos_item': '1',
#     't_s': '20W Type C Mobile Charger Adapter%2C Fast Charging For Android%2C iPhone - RAAP M20',
# }
#
# response = requests.get(
#     'https://www.bigbasket.com/pd/40326744/ambrane-raap-m-20-wall-charger-1-pc/',
#     params=params,
#     cookies=cookies,
#     headers=headers,
# )
#
# print(response.status_code)
# print(response.text)


#
# import requests
#
# cookies = {
#     '_bb_locSrc': 'default',
#     'x-channel': 'web',
#     '_bb_aid': 'MjkxMzA4NDUzMA==',
#     '_bb_cid': '1',
#     '_bb_vid': 'MTA5MjE4ODI0NzM0OTIzODc2Ng==',
#     '_bb_nhid': '7427',
#     '_bb_dsid': '7427',
#     '_bb_dsevid': '7427',
#     '_bb_bhid': '',
#     '_bb_loid': '',
#     'csrftoken': 'LyMBoIEbspXI8F6p6l8qElAKluLRLkhro5B8QTHazWfu2nbn4aFMAD0OsgATjnYM',
#     'isintegratedsa': 'true',
#     'jentrycontextid': '10',
#     'xentrycontextid': '10',
#     'xentrycontext': 'bbnow',
#     '_bb_bb2.0': '1',
#     'is_global': '1',
#     '_bb_addressinfo': '',
#     '_bb_pin_code': '',
#     '_bb_sa_ids': '19224',
#     '_is_tobacco_enabled': '1',
#     '_is_bb1.0_supported': '0',
#     '_bb_cda_sa_info': 'djIuY2RhX3NhLjEwLjE5MjI0',
#     'is_integrated_sa': '1',
#     'is_subscribe_sa': '0',
#     'bb2_enabled': 'true',
#     'bm_ss': 'ab8e18ef4e',
#     'csurftoken': 'l89T5A.MTA5MjE4ODI0NzM0OTIzODc2Ng==.1769166693713.4lI6duImJKQh9JhfAJ1+EJA54IdgaTETSkm9laksWTw=',
#     'bigbasket.com': 'a67c3a2e-c9dc-4db5-a5af-82b52ce70b6e',
#     '_gcl_au': '1.1.1510641153.1769166694',
#     'jarvis-id': '440d5616-af1f-4c22-a8fa-8f7bb9c29a01',
#     'adb': '0',
#     '_gid': 'GA1.2.427618720.1769166695',
#     'ufi': '1',
#     'bm_s': 'YAAQLXLBFwBRkcSbAQAAxv2P6gR42H22POD12AnPqCg2GgiRitttxOGVHETLjNoojjXJPhQXz7gSBuI66ZzNSg78cFA9YS3qUVqu00CaKlp5k6w+1MLqhI2O+KwoVQCHcuig6QMkoGsgRDHcFvBy48R0a/132IvNMNgUChALMhj16A7jPL16q59olLv9x4MSDPujh7o083VxRU4Q/rt0SoQ8oKGc+ImTAPyaHo68KxpY9uA+hJjrC9UzNVA9nArpqOHamC/YRZPN/1sToplvrQ52NBj0mTpgTlH+TTAHzTQEV9hI9NECAAHNN3KI7gFXuIpz4yYydHaOvxskcohuKnoW51nfGofo1HP+V2oONvilecQqJM0KLxF75qOyrHosAPK6wFhQHzg5dFP9UHZWl4GHfDsDhH8pCfPQA9L1VlzSfWbp3vfJsQlz5jnm5pfOYhoCo1nRR4lBctIuDR4qJF5vN/98ylhGl778uvokS7O3LyQFnFCa6m3H7XUtIqnsp7sygoe1dtiis5qUm7Mu8yECvjAcs88n6x7L9xhd5WrNB3dLDTIq0M3ndtMw4xpbAVN7ex3PD65EUTfQGYbutMY=',
#     'bm_so': '7065C8D7DFF124B34158615E92E262BA3AE14A59A44BB98FF7039C283E8E8D15~YAAQLXLBFwFRkcSbAQAAxv2P6gZluCsJqpHoQLzS9Gv7NENaJhfmy9ch2pNiVnoFR4JcCfS09oi5WtgRw1CSdWAN9Bifp+JJ4tKs0N5280jXBziWLOXGoiyUyO8jXtzZf0zTND3AFQgaEEQ0cApaQ33xMS2m4SIJZ4r1EL3OPmO0753YP9mZ3+/Vsv/P53oB5ovQ1VIM7/Hh27rsYzuZ73AiGu0S44i5MNirWXfVoRYoAXeQBtGqsx/fYfci1ETL8svkmWzPqGWQAkE+EGZLbtYGsQDKUheZgGovhJTgtoEXOivr90QQkY447iWa98+OWdWhJe/7e5ievlxrMnrwWJHWIIEnlhzLwPUSut3GyD7v+w35sbWsannLCPTidWYHw1T7m+4x7OiaA8nF3ie87kJDI4ueoLBpEwevtqKBYxKE7UTkoa3RvBhivBxliXuykoE03Abo5vdc3eJRTqFfBoQH',
#     '_ga_FRRYG5VKHX': 'GS2.1.s1769166695$o1$g1$t1769166863$j60$l0$h0',
#     '_ga': 'GA1.2.1557341045.1769166695',
#     'ts': '2026-01-23%2016:44:24.626',
#     'bm_lso': '7065C8D7DFF124B34158615E92E262BA3AE14A59A44BB98FF7039C283E8E8D15~YAAQLXLBFwFRkcSbAQAAxv2P6gZluCsJqpHoQLzS9Gv7NENaJhfmy9ch2pNiVnoFR4JcCfS09oi5WtgRw1CSdWAN9Bifp+JJ4tKs0N5280jXBziWLOXGoiyUyO8jXtzZf0zTND3AFQgaEEQ0cApaQ33xMS2m4SIJZ4r1EL3OPmO0753YP9mZ3+/Vsv/P53oB5ovQ1VIM7/Hh27rsYzuZ73AiGu0S44i5MNirWXfVoRYoAXeQBtGqsx/fYfci1ETL8svkmWzPqGWQAkE+EGZLbtYGsQDKUheZgGovhJTgtoEXOivr90QQkY447iWa98+OWdWhJe/7e5ievlxrMnrwWJHWIIEnlhzLwPUSut3GyD7v+w35sbWsannLCPTidWYHw1T7m+4x7OiaA8nF3ie87kJDI4ueoLBpEwevtqKBYxKE7UTkoa3RvBhivBxliXuykoE03Abo5vdc3eJRTqFfBoQH~1769166894223',
# }
#
# headers = {
#     'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
#     'accept-language': 'en-US,en;q=0.9',
#     'cache-control': 'max-age=0',
#     'priority': 'u=0, i',
#     'sec-ch-ua': '"Not(A:Brand";v="8", "Chromium";v="144", "Google Chrome";v="144"',
#     'sec-ch-ua-mobile': '?0',
#     'sec-ch-ua-platform': '"Windows"',
#     'sec-fetch-dest': 'document',
#     'sec-fetch-mode': 'navigate',
#     'sec-fetch-site': 'same-origin',
#     'sec-fetch-user': '?1',
#     'upgrade-insecure-requests': '1',
#     'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/144.0.0.0 Safari/537.36',
#     # 'cookie': '_bb_locSrc=default; x-channel=web; _bb_aid=MjkxMzA4NDUzMA==; _bb_cid=1; _bb_vid=MTA5MjE4ODI0NzM0OTIzODc2Ng==; _bb_nhid=7427; _bb_dsid=7427; _bb_dsevid=7427; _bb_bhid=; _bb_loid=; csrftoken=LyMBoIEbspXI8F6p6l8qElAKluLRLkhro5B8QTHazWfu2nbn4aFMAD0OsgATjnYM; isintegratedsa=true; jentrycontextid=10; xentrycontextid=10; xentrycontext=bbnow; _bb_bb2.0=1; is_global=1; _bb_addressinfo=; _bb_pin_code=; _bb_sa_ids=19224; _is_tobacco_enabled=1; _is_bb1.0_supported=0; _bb_cda_sa_info=djIuY2RhX3NhLjEwLjE5MjI0; is_integrated_sa=1; is_subscribe_sa=0; bb2_enabled=true; bm_ss=ab8e18ef4e; csurftoken=l89T5A.MTA5MjE4ODI0NzM0OTIzODc2Ng==.1769166693713.4lI6duImJKQh9JhfAJ1+EJA54IdgaTETSkm9laksWTw=; bigbasket.com=a67c3a2e-c9dc-4db5-a5af-82b52ce70b6e; _gcl_au=1.1.1510641153.1769166694; jarvis-id=440d5616-af1f-4c22-a8fa-8f7bb9c29a01; adb=0; _gid=GA1.2.427618720.1769166695; ufi=1; bm_s=YAAQLXLBFwBRkcSbAQAAxv2P6gR42H22POD12AnPqCg2GgiRitttxOGVHETLjNoojjXJPhQXz7gSBuI66ZzNSg78cFA9YS3qUVqu00CaKlp5k6w+1MLqhI2O+KwoVQCHcuig6QMkoGsgRDHcFvBy48R0a/132IvNMNgUChALMhj16A7jPL16q59olLv9x4MSDPujh7o083VxRU4Q/rt0SoQ8oKGc+ImTAPyaHo68KxpY9uA+hJjrC9UzNVA9nArpqOHamC/YRZPN/1sToplvrQ52NBj0mTpgTlH+TTAHzTQEV9hI9NECAAHNN3KI7gFXuIpz4yYydHaOvxskcohuKnoW51nfGofo1HP+V2oONvilecQqJM0KLxF75qOyrHosAPK6wFhQHzg5dFP9UHZWl4GHfDsDhH8pCfPQA9L1VlzSfWbp3vfJsQlz5jnm5pfOYhoCo1nRR4lBctIuDR4qJF5vN/98ylhGl778uvokS7O3LyQFnFCa6m3H7XUtIqnsp7sygoe1dtiis5qUm7Mu8yECvjAcs88n6x7L9xhd5WrNB3dLDTIq0M3ndtMw4xpbAVN7ex3PD65EUTfQGYbutMY=; bm_so=7065C8D7DFF124B34158615E92E262BA3AE14A59A44BB98FF7039C283E8E8D15~YAAQLXLBFwFRkcSbAQAAxv2P6gZluCsJqpHoQLzS9Gv7NENaJhfmy9ch2pNiVnoFR4JcCfS09oi5WtgRw1CSdWAN9Bifp+JJ4tKs0N5280jXBziWLOXGoiyUyO8jXtzZf0zTND3AFQgaEEQ0cApaQ33xMS2m4SIJZ4r1EL3OPmO0753YP9mZ3+/Vsv/P53oB5ovQ1VIM7/Hh27rsYzuZ73AiGu0S44i5MNirWXfVoRYoAXeQBtGqsx/fYfci1ETL8svkmWzPqGWQAkE+EGZLbtYGsQDKUheZgGovhJTgtoEXOivr90QQkY447iWa98+OWdWhJe/7e5ievlxrMnrwWJHWIIEnlhzLwPUSut3GyD7v+w35sbWsannLCPTidWYHw1T7m+4x7OiaA8nF3ie87kJDI4ueoLBpEwevtqKBYxKE7UTkoa3RvBhivBxliXuykoE03Abo5vdc3eJRTqFfBoQH; _ga_FRRYG5VKHX=GS2.1.s1769166695$o1$g1$t1769166863$j60$l0$h0; _ga=GA1.2.1557341045.1769166695; ts=2026-01-23%2016:44:24.626; bm_lso=7065C8D7DFF124B34158615E92E262BA3AE14A59A44BB98FF7039C283E8E8D15~YAAQLXLBFwFRkcSbAQAAxv2P6gZluCsJqpHoQLzS9Gv7NENaJhfmy9ch2pNiVnoFR4JcCfS09oi5WtgRw1CSdWAN9Bifp+JJ4tKs0N5280jXBziWLOXGoiyUyO8jXtzZf0zTND3AFQgaEEQ0cApaQ33xMS2m4SIJZ4r1EL3OPmO0753YP9mZ3+/Vsv/P53oB5ovQ1VIM7/Hh27rsYzuZ73AiGu0S44i5MNirWXfVoRYoAXeQBtGqsx/fYfci1ETL8svkmWzPqGWQAkE+EGZLbtYGsQDKUheZgGovhJTgtoEXOivr90QQkY447iWa98+OWdWhJe/7e5ievlxrMnrwWJHWIIEnlhzLwPUSut3GyD7v+w35sbWsannLCPTidWYHw1T7m+4x7OiaA8nF3ie87kJDI4ueoLBpEwevtqKBYxKE7UTkoa3RvBhivBxliXuykoE03Abo5vdc3eJRTqFfBoQH~1769166894223',
# }
#
# response = requests.get(
#     'https://www.bigbasket.com/pd/40329957/oneplus-nord-ce4-5g-8gb-ram-128gb-chrome-1-n/',
#     cookies=cookies,
#     headers=headers,
# )
#
#
# print(response.status_code)
# print(response.text)
