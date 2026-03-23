import config


def replace_empty_strings(obj):
    """Recursively replace empty strings with NA."""
    if isinstance(obj, dict):
        return {k: replace_empty_strings(v) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [replace_empty_strings(i) for i in obj]
    elif obj == "":
        return "NA"
    else:
        return obj

# process all documents
for doc in config.collection_1.find():
    new_doc = replace_empty_strings(doc)
    config.collection_1.replace_one({"_id": doc["_id"]}, new_doc)

print("All empty strings replaced with 'NA'.")