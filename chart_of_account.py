from bson.objectid import ObjectId
import dateutil.parser
import pymongo
from dataclasses import dataclass,field

import certifi
ca = certifi.where()

# import registration

client = pymongo.MongoClient(f"mongodb+srv://joeysabusido:genesis11@cluster0.r76lv.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.arise_church


class SaveCoa:

    def __init__(self, coa, category):
        self.coa = coa
        self.category = category


    def insert_chartofAccount(coa):
        """
        This function is for
        inserting chart of account
        """
        collection = db['chartOFaccount']
        dataInsert = {
                'chart_of_account': coa.coa,
                'category': coa.category,      
            }
            
        try:
            collection.insert_one(dataInsert)
        
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}") 
    
class test_coa:
    def __init__(self, list_coa):
        self.list_coa = list_coa

    def list_chart_of_account(self):
        """
        This function is for is 
        for querying all record 
        from chartOFaccount table
        """
        a = self.list_coa['chart_of_account']
        b = self.list_coa['category']
       
        return(a+ ' ' + b)

    def print_sample(self) :
        print(self.list_coa['chart_of_account'])





@dataclass
class InsertJournal:
    
    
    date: str
    charofAccount: str
    amount: float
    particular: str


    def insert_journal(journal):
        """
        This function is for
        inserting chart of account
        """
        collection = db['journal_entry']
        dataInsert = {
                'date': journal.date,
                'chart_of_account': journal.charofAccount, 
                'amount': journal.amount,
                'particular': journal.particular,     
            }
            
        try:
            collection.insert_one(dataInsert)
        
        except Exception as ex:
            print("Error", f"Error due to :{str(ex)}")

    def journal_entryList(self):
        """
        This is for calling 
        all the list of journal
        """
        pass

# collection = db['journal_entry']  
# agg_result = collection.find().sort('date', pymongo.ASCENDING)  

# jourNal_entry={}
# for x in agg_result:
#     data = {    
#             'date': x['date'],
#             'chart_of_account': x['chart_of_account'],
#             'amount': x['amount'],
#             'particular': x['particular'],
                
#             }
      
#     jourNal_entry.update(data)   
        
        


    
