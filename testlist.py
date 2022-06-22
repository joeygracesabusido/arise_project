from dataclasses import dataclass,field
from typing import List

import pymongo
import certifi
ca = certifi.where()

# import registration

client = pymongo.MongoClient(f"mongodb+srv://joeysabusido:genesis11@cluster0.r76lv.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.arise_church



@dataclass
class journal_entry:
    
    
    date: str
    charofAccount: str
    amount: float
    particular: str


class list_chartAccount:

  def __init__(self) -> None:
    self.employees: List[journal_entry] = []

  def find_Manager(self) :
    manager=[]
    for i in self.employees:
      if i.charofAccount == 'Tithes Income':
        manager.append(i)
    return manager

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

print(list_chartAccount.find_Manager())  
    
      
 