from pymongo import MongoClient
from datetime import datetime

client = MongoClient('mongodb://XB-3619:4adHheb1Y&TN6%21PW%23gD@15.235.80.77:27017/?authSource=admin')
db = client['XB_3619_quickcommerce_india_api']
input = db['input_keywords']
collection_1 = db['bigbasket_data']

run_date = datetime.now().strftime("%Y_%m_%d")
run_date_1 = datetime.now().strftime("%Y-%m-%d %H:%M:%S")