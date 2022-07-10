from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.pok6t.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

Jason = {
    "student_id":"1009",
   "first_name": "Jason",
   "last_name": "Yona",
      "enrollments": [
        {
        "term":"Summer 2022",
        "start_date":"August 12, 2022",
        "end date": "June 5, 2022",
        "gpa":"3.9",
        "courses": [
        {
            "course_id":"BS 110",
            "description":"A course about personal finances.",
            "instructor":"Somya Valsh",
            "grade":"A"
        }
        ]
        }
   ]
}

students = db.students


Jason_student_id = students.insert_one(Jason).inserted_id


print(str(Jason_student_id))
print("This is Alex's ID")

print("All information has been inserted into database.")