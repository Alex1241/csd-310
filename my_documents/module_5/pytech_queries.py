from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.pok6t.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech


docs = db.students.find({})
doc = db.students.find_one({"student_id": "1006"})

for doc in docs:
    print(doc)


    print("Extracting data such as student_id and name from document...")
    print(doc["student_id"] + " " + doc["first_name"] + " " + doc["last_name"])