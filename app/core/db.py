import json

def load_json_db():
    try:
        with open('./db/items.json', 'r') as file:
            data = json.load(file)
        print("JSON database loaded successfully")
        return data
    
    except FileNotFoundError:
        print("File Not found")
    except json.JSONDecodeError:
        print("Malformed JSON, unable to decode")