from pymongo import MongoClient
client = MongoClient('mongodb://127.0.0.1:27017/')
db=client['NewDB']
info = db.dbinformation   # create collection name dbinformation
record = {'name':'sagar','lastname':'kadam'}
info.insert_one(record)   # insert single record

# redords = [{'name':'sagar,'lastname':'kadam'}, {'name':'sagar,'lastname':'kadam'}]
# info.insert_many(records)
