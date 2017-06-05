import sys
import pymongo

connection = pymongo.MongoClient("mongodb://localhost")

db = connection.test
users = db.users

doc = {'firstname':'Alex','lastname':'Li'}
print(doc)
print("About to insert the document")

try:
    users.insert_one(doc)
except Exception as e:
    print("insert failed: ",e)

print(doc)
print("inserting again")

try:
    users.insert_one(doc)
except Exception as e:
    print("second insert failed: ",e)
