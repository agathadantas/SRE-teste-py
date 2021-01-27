from pymongo import MongoClient

client = MongoClient("localhost", 27017)
print(client.list_database_names())

db = client.Cats

db.teste.insert_many(
    [
        {"id": 1},
        {"id": 2},
        {"id": 3}

    ]
)
