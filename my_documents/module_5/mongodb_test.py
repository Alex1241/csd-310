from pymongo import MongoClient

url ="mongodb+srv://admin:admin@cluster0.pok6t.mongodb.net/pytech?retryWrites=true&w=majority";
client = MongoClient(url)
db = client.pytech

print(db.list_collection_names)