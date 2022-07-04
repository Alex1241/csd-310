from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.pok6t.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

fred = {
    "student_id":"1006",
   "first_name": "Fred",
   "last_name": "Ava",
   "enrollments": [
        {
        "term":"Spring 2022",
        "start_date":"March 5, 2022",
        "end date": "June 5, 2022",
        "gpa":"3.9",
        "courses": [
            {
            "course_id":"GD110",
            "description":"Course about design basics for graphics.",
            "instructor":"Allen York",
            "grade":"A"
            }
        ]
        }
   ]
}

joe = {
    "student_id":"1007",
   "first_name": "Joe",
   "last_name": "Yer",
    "enrollments": [
        {
        "term":"Spring 2022",
        "start_date":"March 5, 2022",
        "end date": "June 5, 2022",
        "gpa":"4.0",
        "courses": [
            {
            "course_id":"AR111",
            "description":"Course about art.",
            "instructor":"Kristin Weaver",
            "grade":"A"
         }
        ]
        }
   ]
}

alex = {
    "student_id":"1008",
   "first_name": "Alex",
   "last_name": "Vo",
      "enrollments": [
        {
        "term":"Summer 2022",
        "start_date":"August 12, 2022",
        "end date": "June 5, 2022",
        "gpa":"4.0",
        "courses": [
        {
            "course_id":"CYBR410",
            "description":"Course database security.",
            "instructor":"Bell Derreaver",
            "grade":"A-"
        }
        ]
        }
   ]
}

students = db.students

fred_student_id = students.insert_one(fred).inserted_id
joe_student_id = students.insert_one(joe).inserted_id
alex_student_id = students.insert_one(alex).inserted_id

print(str(fred_student_id))
print("This is Fred's ID")
print(str(joe_student_id))
print("This is Joe's ID")
print(str(alex_student_id))
print("This is Alex's ID")

print("All information has been inserted into database.")