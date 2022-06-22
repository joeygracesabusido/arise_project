from dataclasses import dataclass,field
import pymongo
import certifi
ca = certifi.where()

# import registration

client = pymongo.MongoClient(f"mongodb+srv://joeysabusido:genesis11@cluster0.r76lv.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.arise_church




class Person:
  def __init__(self, name, age):
    self.name = name
    self.age = age


  def printName(abc):
    print("Your Name is " + abc.name, "Your age is " + abc.age )


class testCoa:
  def __init__(self, name, name2):
      self.name = name
      self.name2 = name2


  def insert_chartofAccount(coa):
    print("Chart of Account " + coa.name, " Category " + coa.name2 )




@dataclass
class journal_entry:
    
    
    date: str
    charofAccount: str
    amount: float
    particular: str
    
    def __str__(self):
           return f'{self.date} {self.charofAccount} {self.amount}'




   

