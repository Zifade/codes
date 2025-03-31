
from flask import Flask, render_template
import os # importing operating system module
import pymongo
from bson.objectid import ObjectId
MONGODB_URI = 'mongodb+srv://jorgelutz1:XHIz5HzUCo1cXJ7t@30daysofpython.e9nc9fv.mongodb.net/?retryWrites=true&w=majority&appName=30DaysOfPython'
client = pymongo.MongoClient(MONGODB_URI)
print(client.list_database_names())

# Creating database
db = client.thirty_days_of_python
# Creating students collection and inserting a document
"db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})"
print(client.list_database_names())
"""
students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
for student in students:
    db.students.insert_one(student)

"""
#crear database
"db = client['thirty_days_of_python']" # accessing the database

#crear collection e insertar document
"""
db.students.insert_one({'name': 'Asabeneh', 'country': 'Finland', 'city': 'Helsinki', 'age': 250})
print(client.list_database_names())
"""

#insertar muchos documentos
"""
students = [
        {'name':'David','country':'UK','city':'London','age':34},
        {'name':'John','country':'Sweden','city':'Stockholm','age':28},
        {'name':'Sami','country':'Finland','city':'Helsinki','age':25},
    ]
for student in students:
    db.students.insert_one(student)
"""

#find
students = db.students.find()
"""
students = db.students.find({}, {"_id":0,  "name": 1, "country":1}) # 0 means not include and 1 means include
for student in students:
    print(student)
"""

#find con query
"""
query = {
    "country":"Finland"
}
students = db.students.find(query)

for student in students:
    print(student)
"""

#find con query with modifier
"""
query = {"age":{"$gt":30}}
students = db.students.find(query)
for student in students:
    print(student)
"""
#find and sort
"""
students = db.students.find().sort('name')
for student in students:
    print(student)


students = db.students.find().sort('name',-1)
for student in students:
    print(student)
"""

#update con query
"""
query = {'age':250}
new_value = {'$set':{'age':38}}

db.students.update_one(query, new_value)
# lets check the result if the age is modified
for student in db.students.find():
    print(student)
"""

#delete document
"""
query = {'age':250}
db.students.delete_one(query)

for student in db.students.find():
    print(student)
"""

#drop collection
"""
db.students.drop()
"""
app = Flask(__name__)
if __name__ == '__main__':
    # for deployment we use the environ
    # to make it work for both production and development
    port = int(os.environ.get("PORT", 5000))
    app.run(debug=True, host='0.0.0.0', port=port)