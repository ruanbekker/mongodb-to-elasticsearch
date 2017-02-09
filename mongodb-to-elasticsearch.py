import time
from pymongo import MongoClient
from elasticsearch import Elasticsearch

mongodb_client = MongoClient('mongodb://10.0.1.11:27017')
es_client = Elasticsearch(['http://10.0.1.12:9200'])

mdb = mongodb_client['mydb']

drop_index = es_client.indices.create(index='myindex', ignore=400)
create_index = es_client.indices.delete(index='myindex', ignore=[400, 404])

data = mdb.mycollection.find()

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

    res = es_client.index(index="myindex", doc_type="docs", body=doc)
    time.sleep(0.2)

print("Done")
