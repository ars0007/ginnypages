from flask_pymongo import pymongo


def get_client(database):
    client = pymongo.MongoClient("localhost", 27017)
    db = client.get_database(database)
    return db


class GenericDao:
    def __init__(self, collection_name):
        self.client = get_client("ginnypages")[collection_name]
        self.collection = collection_name

    def find_one_record(self, filter_query, projection={}):
        record = self.client.find_one(filter_query, projection)
        return record

    def find_records(self, filter_query={}, projection={}):
        all_records = []
        records = self.client.find(filter_query, projection)
        for record in records:
            all_records.append(record)
        return all_records

    def insert_record(self, document):
        curser = self.client.insert_one(document)
        return curser.acknowledged

    def delete_record(self, filter_query, projection={}):
        record = self.client.find_one_and_delete(filter_query, projection)
        return record

    def update_record(self, document, filter_query={}, projection={}):
        record = self.client.find_one_and_update(filter_query, {"$set": document}, projection)
        return record
