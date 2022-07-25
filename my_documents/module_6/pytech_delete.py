from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.pok6t.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech
docs = db.students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs:
    print("Student ID: " + doc["student_id"])
    print("First Name: " + doc["first_name"])
    print("Last Name: " + doc["last_name"])

John = {
    "student_id":"1010",
   "first_name": "John",
   "last_name": "Doe",
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
John_student_id = students.insert_one(John).inserted_id
doc10 = db.students.find_one({"student_id": "1010"})

print("-- INSERT STATEMENTS --")
print("Inserted Student record John Doe into the students collection with document_id",  doc10["_id"]) 
print("-- DISPLAYING STUDENT TEST DOC --")
print("Student ID: " + doc10["student_id"])
print("First Name: " + doc10["first_name"])
print("Last Name: " + doc10["last_name"])

deleteStudent = db.students.delete_one({"student_id":"1010"})

#docs2 is made to fix the issue with the code not printing the list of students again
docs2 = db.students.find({})

print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
for doc in docs2:
    print("Student ID: " + doc["student_id"])
    print("First Name: " + doc["first_name"])
    print("Last Name: " + doc["last_name"])

input("End of program, press any key to continue...")