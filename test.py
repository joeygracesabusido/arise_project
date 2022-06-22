from bson.objectid import ObjectId
import dateutil.parser

from dataclasses import dataclass,field
from typing import List
import pymongo
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
# from pythonClass import journal_entry

from testlist import list_chartAccount, journal_entry

def main_data():
    """
    this function is for main 
    data for journal Entry
    """
    
    collection = db['journal_entry']  
    agg_result = collection.find()  

    
    jourNal_entry={}
    for x in agg_result:
        data = {    
                'date': x['date'],
                'chart_of_account': x['chart_of_account'],
                'amount': x['amount'],
                'particular': x['particular'],
                    
                }
          
        jourNal_entry.update(data)
        global listJournal
        listJournal = journal_entry(jourNal_entry['date'],
                                      jourNal_entry['chart_of_account'],
                                      jourNal_entry['amount'],
                                      jourNal_entry['particular'])
        print(listJournal)

    print(list_chartAccount.find_Manager(listJournal))


    
   

# collection = db['chartOFaccount']
# query = collection.find()

# listCOA = {}
# Test_list = ''
# count = 0
# for i in query:
    
   
#     data = {
            
#             'chart_of_account': i['chart_of_account'],
#             'category': i['category'],
            
#         }
    
#     listCOA.update(data)

    
#     Test_list =test_coa(listCOA)  

#     Test_list.print_sample()

main_data()
