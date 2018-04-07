import time
from pymongo import MongoClient

mdb_src_client = MongoClient('mongodb://user:pass@db1.mongodb.com:27017/admin?authMechanism=SCRAM-SHA-1')
mdb_dst_client = MongoClient('mongodb://user:pass@db2.mongodb.com:27017/admin?authMechanism=SCRAM-SHA-1')

mdb_src_db = mdb_src_client['flask_reminders']
mdb_dst_db = mdb_dst_client['flask_reminders']

data = mdb_src_db.reminders.find()

mdb_dst_col = mdb_dst_db['reminders']

for x in data:
    _date = x['date']
    _type = x['type']
    _category = x['category']
    _description = x['description']
    _link = x['link']

    doc = {
        'date': _date,
        'type': _type,
        'category': _category,
        'description': _description,
        'link': _link
    }

    res = mdb_dst_col.insert_one(doc).inserted_id
    print(res)
    time.sleep(1)

print("Done")
