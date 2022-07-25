from pymongo import MongoClient

url = "mongodb+srv://admin:admin@cluster0.pok6t.mongodb.net/pytech?retryWrites=true&w=majority"
client = MongoClient(url)
db = client.pytech

#Search and Print Section
docs = db.students.find({})
doc = db.students.find_one({"student_id": "1007"})
doc2 = db.students.find_one({"student_id": "1008"})
doc3 = db.students.find_one({"student_id": "1009"})

#Print section before alterations
print("-- DISPLAYING STUDENTS DOCUMENTS FROM find() QUERY --")
print("Student ID: " + doc["student_id"])
print("First Name: " + doc["first_name"])
print("Last Name: " + doc["last_name"])

print("Student ID: " + doc2["student_id"])
print("First Name: " + doc2["first_name"])
print("Last Name: " + doc2["last_name"])

print("Student ID: " + doc3["student_id"])
print("First Name: " + doc3["first_name"])
print("Last Name: " + doc3["last_name"])

#Update Information Section
result = db.students.update_one({"student_id": "1007"}, {"$set": {"last_name": "Carlson"}})
result2 = db.students.update_one({"student_id": "1008"}, {"$set": {"last_name": "Pohtree"}})
result3 = db.students.update_one({"student_id": "1009"}, {"$set": {"last_name": "Elison"}})

#Printer Section 2
print("-- INSERT STATEMENTS --")
print("Updated Student record Joe Yer into the students collection with document_id ",  doc)
print("Updated Student record Alex Vo into the students collection with document_id ",  doc2)
print("Updated Student record Jason Yona into the students collection with document_id ",  doc3)

#Update Variables Section
doc = db.students.find_one({"student_id": "1007"})
doc2 = db.students.find_one({"student_id": "1008"})
doc3 = db.students.find_one({"student_id": "1009"})

#Print section 3
print("-- DISPLAYING STUDENT DOCUMENT 1007 --")
print("Student ID: " + doc["student_id"])
print("First Name: " + doc["first_name"])
print("Last Name: " + doc["last_name"])

print("-- DISPLAYING STUDENT DOCUMENT 1008 --")
print("Student ID: " + doc2["student_id"])
print("First Name: " + doc2["first_name"])
print("Last Name: " + doc2["last_name"])

print("-- DISPLAYING STUDENT DOCUMENT 1009 --")
print("Student ID: " + doc3["student_id"])
print("First Name: " + doc3["first_name"])
print("Last Name: " + doc3["last_name"])

input("End of program, press any key to continue...")