import pymongo
from pymongo import MongoClient



client = MongoClient('localhost', 27017)

db = client.test_database
collection = db.test_collection

student = {
 'id': '20170101',
 'name': 'Jordan',
 'age': 20,
 'gender': 'male'
}
student2 = {
 'id': '20170202',
 'name': 'Mike',
 'age': 21,
 'gender': 'male'
}
#插入数据：
# result1 = collection.insert_one(student)
# print(result1)
result3 = collection.insert_many([student,student2])
print(result3)
#查找数据：
result2 = collection.find_one({'name': 'Mike'})
print(result2)
print(db.collection_names())