from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017/')
db=client['NewDB']
info = db.dbinformation   # create collection name dbinformation
# record = {'name':'sagar','lastname':'kadam'}
# info.insert_one(record)   # insert single record

records = [{'name':'Ram','lastname':'Charan', 'age':22},
             {'name':'Raj','lastname':'Rane','age':24},
             {'name':'Sham','lastname':'Naik','age':25}]
info.insert_many(records)
