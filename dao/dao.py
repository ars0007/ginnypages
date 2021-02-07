from  flask_pymongo import  pymongo

# CONNECTION_STRING = "mongodb+srv://admin:admin#0007@cluster0.cz5ig.mongodb.net/<dbname>?retryWrites=true&w=majority"
# client = pymongo.MongoClient(CONNECTION_STRING)
# database = client.get_database("confluence")
# collection = pymongo.collection.Collection("users")

def connect_database(connection_string, database, collection_name):
    client = pymongo.MongoClient(connection_string)
    db = client.get_database(database)
    collection = pymongo.collection.Collection(db, collection_name)
    return  collection


def find_one_record():
    pass

def find_records():
    pass



