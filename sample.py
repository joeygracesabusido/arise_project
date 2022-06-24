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
    def find(collection):
        return Database.DATABASE[collection].find()

    @staticmethod
    def find_one(collection,query):
        return Database.DATABASE[collection].find(query)