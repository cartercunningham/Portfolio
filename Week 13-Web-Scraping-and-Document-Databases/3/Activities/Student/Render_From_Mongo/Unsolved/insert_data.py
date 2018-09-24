import pymongo
conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)
db = client.store_inventory
collection=db.produce
db.collection.insert_many [{"type": "apples","cost": .23,"stock": 333},{"type": "oranges","cost": .45,"stock": 444},{"type": "potatoes","cost": .67,"stock": 555}]