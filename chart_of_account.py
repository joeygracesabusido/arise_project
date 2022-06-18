from bson.objectid import ObjectId
import dateutil.parser
import pymongo

import certifi
ca = certifi.where()

# import registration

client = pymongo.MongoClient(f"mongodb+srv://joeysabusido:genesis11@cluster0.r76lv.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.arise_church


class testCoa:

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
    
class list_coa:
    def __init__(self, list_coa):
        self.list_coa = list_coa
       
    def list_chart_of_account(self):
        """
        This function is for is 
        for querying all record 
        from chartOFaccount table
        """
    
        collection = db['chartOFaccount']
        query = collection.find()

        a = ''
        for i in query:
            a = i['chart_of_account']
            return self.a
      
       
        
        


    
