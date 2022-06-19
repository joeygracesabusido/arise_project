from bson.objectid import ObjectId
import dateutil.parser
import pymongo
from dataclasses import dataclass,field

import certifi
ca = certifi.where()

# import registration

client = pymongo.MongoClient(f"mongodb+srv://joeysabusido:genesis11@cluster0.r76lv.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.arise_church

# from pythonClass import Person

# name1 = input("Enter your Name: ")
# age2 = input("Enter your age:")

# p1 = Person(name1,age2)


# p1.printName()

# from pythonClass import testCoa

# name1 = input("Enter Chart of Account: ")
# age2 = input("Enter category:")

# p1 = testCoa(name1,age2)


# p1.insert_chartofAccount()

from chart_of_account import test_coa

collection = db['chartOFaccount']
query = collection.find()

listCOA = {}
Test_list = ''
count = 0
for i in query:
    
   
    data = {
            
            'chart_of_account': i['chart_of_account'],
            'category': i['category'],
            
        }
    
    listCOA.update(data)

    
    Test_list =test_coa(listCOA)  

    Test_list.print_sample()

