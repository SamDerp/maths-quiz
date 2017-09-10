from pymongo import MongoClient
from pprint import pprint


class AdminMongo(object):
    def __init__(self):
        self.client = MongoClient()

    def delete_entire_database(self):
        deletedDatabase = str(input("What is the name of the database you wish to delete: "))
        self.client.drop_database(deletedDatabase)

    def list_all_databases(self):
        pprint(self.client.database_names())
