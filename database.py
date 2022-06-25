from dataclasses import dataclass,field
from pickle import NONE
from typing import List

import pymongo
import certifi
ca = certifi.where()


class Database(object):
    URI = "mongodb+srv://joeysabusido:genesis11@cluster0.r76lv.mongodb.net/?retryWrites=true&w=majority"
    DATABASE = NONE

    def initialize():
        client = pymongo.MongoClient(Database.URI)
        Database.DATABASE = client.arise_church
        
    @staticmethod
    def find_all(collection):
        return Database.DATABASE[collection].find()

    @staticmethod
    def find_one(collection,query):
        """
        This function is
        querying 
        """
        return Database.DATABASE[collection].find(query)

    @staticmethod
    def update_approval(collection, query, newValue):
        """
        This function is for updating
        """
        return Database.DATABASE[collection].update_many(query, newValue)

    @staticmethod
    def search_members_data_file(collection):
        return Database.DATABASE[collection].find()

    @staticmethod
    def search_count(collection,query):
        return Database.DATABASE[collection].count_documents(query)

