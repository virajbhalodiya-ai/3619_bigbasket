from datetime import datetime
import pandas as pd
from pymongo import MongoClient
import os

# Get today's date in YYYY_MM_DD format
today_date = datetime.today().strftime('%Y_%m_%d')

# MongoDB connection
client = MongoClient('mongodb://admin:tP_kc8mn@localhost:27017/?authSource=admin')
db = client['bigbasket']
collection_2 = db['pdp_data']

# Directory and Excel file path
directory = r"D:\Harsh Sir\[XB3619]"
excel_file = os.path.join(directory, f"Bigbasket_{today_date}.xlsx")

# Check if the directory exists, if not, create it
if not os.path.exists(directory):
    os.makedirs(directory)

# Check if the Excel file already exists
if not os.path.exists(excel_file):
    try:
        # Fetch data from MongoDB
        items = list(collection_2.find({}, {"_id": 0}))  # Exclude _id field

        if not items:
            print("No data found in the collection.")
        else:
            # Define the column header sequence (leave blank, fill later)
            header_sequence = [
                "id", "product_title", "brand", "main_image", "category", "Pincode", "availability",
                "msrp", "thumbnail_image_url", "detail_page_images", "Platform url of the SKU",
                "detail_data"
            ]

            # Convert to DataFrame
            if header_sequence:
                df = pd.DataFrame(items, columns=header_sequence)
            else:
                df = pd.DataFrame(items)  # Keep MongoDB order if no header_sequence provided

            # Save to Excel
            df.to_excel(excel_file, index=False)
            print(f"Excel file created successfully: {excel_file}")

    except Exception as e:
        print(f"Error occurred while creating the Excel file: {e}")
else:
    print(f"Excel file already exists at {excel_file}. Skipping creation.")
