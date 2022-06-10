from bson.objectid import ObjectId
import dateutil.parser
import pymongo
import re
from datetime import date
import datetime
import pwinput
from prettytable import PrettyTable

from datetime import datetime

from pymongo import MongoClient
import pandas as pd

from tabulate import tabulate

from matplotlib import pyplot as plt
import numpy as np

import certifi
ca = certifi.where()

# import registration

client = pymongo.MongoClient(f"mongodb+srv://joeysabusido:genesis11@cluster0.r76lv.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.arise_church




def log_in():
    """
    this is for login
    """
    userName = input('Enter Username: ')

   

    dataSearch = db['admin_login']

            
    query = {'username': userName, 'password':pwinput.pwinput()}
    agg_result = dataSearch.find(query)
    
    a = ''
    for x in agg_result:
        a = x['username']
        return selection()
    
   

def selection():
    """
    This function is for selections
    of transaction
    """

    arr = [
            ['1001- Insert Church Ministry'],
            ['1002- Insert Member Details'],
            ['1003- Members List'],
            ['1004- Members Attendance'],
            ['1005- List of Attendae'],
            ['1006- Membership Chart'],
            ['1007- Absent'],
            ]

    # print('1001- Insert Church Ministry')
    # print('1002- Insert Member Details')

    # print(arr)

    print(tabulate(arr, headers =['Code'], tablefmt='psql'))

    ans = input('Please enter code for your Desire transaction: ')


    if ans =='1001':
        return church_ministry()

    if ans =='1002':
        return insert_churchMember()

    if ans =='1003':
        return members_list()

    if ans =='1004':
        return insert_attendace()
    
    if ans =='1005':
        return attendance_list()
    if ans =='1006':
        return report_piechart()
    if ans =='1007':
        return absent_member()

def absent_member():
    """
    This function is for 
    checking the absent
    """

    # dataSearch = db['church_ministry']
    # search_data = dataSearch.find()
   
           
    # church_member=[]
    
    # for value in search_data:
    #     church_member.append(value['ministry'])

    dataSearch2 = db['members_detail']
    search_data2 = dataSearch2.find()

    a = ''
    
    subtitle2=[]
    for i in search_data2:
        a = i['members_id']
        c = i['lname'] + ' , ' + i['fname']


        dataSearch3 = db['attendance']

        # search_data3= dataSearch3.find({'members_id': { "$nin": [a, "" ] } })
        search_data3= dataSearch3.find()
        for value in search_data3:
            b = value['members_id']
            if b !=a:
                subtitle2.append(c)

        # for i in subtitle2:
        #     print(i)
        
    lst_of_lst = []
    for i in subtitle2:
        spl = i.split(',')
        lst_of_lst.append(spl)

    print(tabulate(lst_of_lst, headers =['Name',], tablefmt='psql'))
            
    # print(*subtitle2,sep = "\n")

def attendance_list():
    """
    this is for list of attendance 
    as of today
    """
    today = date.today()
    date_time_str = today.strftime("%Y-%m-%d")
    print(date_time_str)

    date_search = input('Enter Date : ')
    timeNow = ('00:00:00')
    date_time_str2 = date_search + ' ' + timeNow

    # date_time_obj = datetime.strptime(date_search, '%Y-%m-%d').date()
    # date_time_obj = datetime.strptime(date_time_str2, '%Y-%m-%d %H:%M:%S')

    dataSearch = db['attendance']
    
    query = {'date': date_search}
    search_data = dataSearch.find(query)

   
    members ={}
    for row in search_data:
        members.update({row['_id']:
        {
            'members_id': row['members_id'],
            'lname': row['lname'],
            'fname': row['fname'],
            'ministry': row['ministry'],
        }
        })


    menu = PrettyTable()
    menu.field_names=['Count','ID','ID Number','Last Name','First Name', 'Ministry']
    count = 0   
    for emp in members:
        count+=1
        menu.add_row([count,emp,
                    members[emp]['members_id'],
                    members[emp]['lname'],
                    members[emp]['fname'],
                    members[emp]['ministry']
                    
                    ])
                                
    print(menu)
    selection()

def insert_attendace():
    """
    This function is for 
    inserting church attendance
    """
   

    # this is for member's list to get the id number 

    dataSearch = db['members_detail']
    search_data = dataSearch.find().sort('lname', 1)

    
    members ={}
    for row in search_data:
        members.update({row['_id']:
        {
            'members_id': row['members_id'],
            'lname': row['lname'],
            'fname': row['fname'],
            'ministry': row['ministry'],
        }
        })


    menu = PrettyTable()
    menu.field_names=['Count','ID','ID Number','Last Name','First Name', 'Ministry']
    count = 0   
    for emp in members:
        count+=1
        menu.add_row([count,emp,
                    members[emp]['members_id'],
                    members[emp]['lname'],
                    members[emp]['fname'],
                    members[emp]['ministry']
                    
                    ])
                                
    print(menu)


    
# this is for inserting attendance for church member
    dataSearch = db['members_detail']
    query = input('Enter Members ID. ')

   

    searchData = dataSearch.find({'members_id':query})

    members_id = ''
    lastName = ''
    firstName = ''
    ministry = ''

    today = date.today()
    date_time_str = today.strftime("%Y-%m-%d")
    for i in searchData:
        members_id = i['members_id']
        lastName = i['lname']
        firstName = i['fname']
        ministry = i['ministry']


        collection = db['attendance']

        dataInsert = {
            'members_id': members_id,
            'lname': lastName,
            'fname': firstName,
            'ministry':ministry,
            'date': date_time_str,
            'created':datetime.now()
            
        }
        
        try:
            collection.insert_one(dataInsert)
            print('data has been saved')
            selection()
        except Exception as ex:
                    print("Error", f"Error due to :{str(ex)}")


       




def insert_churchMember():
    """
    This function is for
    inserting church Member
    """
    contact_num = ''
    lastName = input('Enter Last name : ')
    firstName = input('Enter First name : ')
    address = input('Enter Address : ')
    date_of_Birth = input('Enter Birth Day: ')
    timeNow = ('00:00:00')
    date_time_str2 = date_of_Birth + ' ' + timeNow

    date_time_obj = datetime.strptime(date_of_Birth, '%m-%d-%Y').date()
    today = date.today()
    age = today.year - date_time_obj.year - ((today.month, today.day) < (date_time_obj.month, date_time_obj.day))

    
    date_time_obj = datetime.strptime(date_time_str2, '%m-%d-%Y %H:%M:%S')

    
    print(f'Your Age: {age}')
    list_ministry()
    ministry = input('Enter Ministry Belong : ')
    contact_num = input('Enter Contact No.  ')


    dataSearch = db['members_detail']
    # agg_result = dataSearch.find({'ref': {"$regex": "^APV"}}).sort('ref',-1).limit(1)
    agg_result = dataSearch.find({'members_id': {"$regex": "AFGM"}}).sort('members_id',-1).limit(1)

    

    a = ""
    for x in agg_result :
        a = x['members_id']


    
    if a =="":
        test_str = ('AFGM-000')
        # test_str = 'APV-000'
        res = test_str

       
        
        
    
    else:
        

        reference_manual = a 
        res = re.sub(r'[0-9]+$',
                lambda x: f"{str(int(x.group())+1).zfill(len(x.group()))}", 
                reference_manual)




    collection = db['members_detail']
    
    if contact_num =='':
        contact_num = 'none'
    else:
        contact_num = contact_num
    dataInsert = {
        'members_id': res,
        'lname': lastName,
        'fname': firstName,
        'address': address,
        'birthday': date_time_obj,
        'age': int(age),
        'ministry': ministry,
        'contact_num': contact_num
          
    }
    
    try:
        collection.insert_one(dataInsert)
        print('data has been saved')
        selection()
    except Exception as ex:
                print("Error", f"Error due to :{str(ex)}")


def members_list():
    """
    This function is for member
    List
    """

    dataSearch = db['members_detail']
    search_data = dataSearch.find().sort('lname', 1)

    # for x in search_data:
    #     a = x['_id']
    #     print(a)

    # listCusor = list(search_data)
    #         # print(listCusor)

    # df = pd.DataFrame(listCusor)
    # # test = df.head()
    # print(df)
    # print(tabulate(search_data, headers =['A','B','C',"D",'E'], tablefmt='psql'))
    members ={}
    for row in search_data:
        members.update({row['_id']:
        {
            'members_id': row['members_id'],
            'lname': row['lname'],
            'fname': row['fname'],
            'ministry': row['ministry'],
        }
        })


    menu = PrettyTable()
    menu.field_names=['Count','ID','ID Number','Last Name','First Name', 'Ministry']
    count = 0   
    for emp in members:
        count+=1
        menu.add_row([count,emp,
                    members[emp]['members_id'],
                    members[emp]['lname'],
                    members[emp]['fname'],
                    members[emp]['ministry']
                    
                    ])
                                
    print(menu)
    selection()
    # print(tabulate(search_data, headers =['Code'], tablefmt='psql'))

def church_ministry():
    """
    This function is for
    inserting church ministry
    """

    c_ministry = input(str('Enter Church Ministry: '))
   
    
    collection = db['church_ministry']
    
    dataInsert = {
        'ministry': c_ministry
       
        
    }
    
    try:
        collection.insert_one(dataInsert)
        print('data has been saved')
        selection()
    except Exception as ex:
                print("Error", f"Error due to :{str(ex)}")

def insert_login_():
    """
    This function is for
    inserting church ministry
    """

    userName = input(str('Enter userName: '))
    password = input('Enter Password: ')

   
    
    collection = db['admin_login']
    
    dataInsert = {
        'userName': userName,
        'Password': password
       
        
    }
    
    try:
        collection.insert_one(dataInsert)
        print('data has been saved')
    except Exception as ex:
                print("Error", f"Error due to :{str(ex)}")


def list_ministry():
    """
    this function is for
    querying church Ministry
    """

    # apv_num = input('Enter APV number : ')
    # dataSearch = db['journal_entry']
    # query = {'ref':apv_num}

    dataSearch = db['church_ministry']

    try:
            search_data = dataSearch.find()
            listCusor = list(search_data)
            # print(listCusor)

            df = pd.DataFrame(listCusor)
            # test = df.head()
            print(df)
        
        

    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}") 


def testing():
    """
    this function is for Testing
    """

    date_time_str = input('Enter Date: ')
    timeNow = ('00:00:00')
    date_time_str2 = date_time_str + ' ' + timeNow
    # print(date_time_str2)

    date_time_obj = datetime.strptime(date_time_str, '%m-%d-%Y').date()
    today = date.today()
    age = today.year - date_time_obj.year - ((today.month, today.day) < (date_time_obj.month, date_time_obj.day))

    # date_time_obj = datetime.strptime(date_time_str, '%m-%d-%Y').date()
    # date_time_obj = datetime.strptime(date_time_str2, '%m-%d-%Y %H:%M:%S')
    
    # print ("The type of the date is now", type(date_time_obj))
    print(f"Your Age : ",{age} )

def call_array():
    """
    this function is for 
    calling a function for list purposes
    """
    dataSearch = db['church_ministry']

    try:
            search_data = dataSearch.find()
            # ministry_list = [k for k in search_data]
            # print(ministry_list)
            # subtitle=[]
            # for value in search_data:
            #     subtitle.append(value['ministry'])
            # print(subtitle)

            a = ''
            search_data2 = 0
            subtitle=[]
            for i in search_data:
                a = i['ministry']

                dataSearch2 = db['members_detail']

                search_data2 = dataSearch2.count_documents({'ministry':a})
                subtitle.append(search_data2)
            print(subtitle)

               
               
                
              



            

            # listCusor = list(search_data)

            # print(listCusor[0]['ministry'])
            # list_a = []
            # for i in search_data:
            #     a = i['ministry']
            #     list_a.append(a)
            #     print(list_a)

            # employee = {}

            # for row in search_data:
            
            #     data = {
            #         'ministry': row['ministry'],
                    
            #     }
            #     employee.update(data)
            #     print(employee)
    except Exception as ex:
        print("Error", f"Error due to :{str(ex)}")

def report_piechart():
    """
    this function is to test pie chart

    """
    dataSearch = db['church_ministry']
    search_data = dataSearch.find()
   
            # ministry_list = [k for k in search_data]
            # print(ministry_list)
    subtitle=[]
    
    for value in search_data:
        subtitle.append(value['ministry'])

    dataSearch2 = db['church_ministry']
    search_data2 = dataSearch2.find()

    a = ''
    
    subtitle2=[]
    for i in search_data2:
        a = i['ministry']
        

        dataSearch3 = db['members_detail']

        search_data3= dataSearch3.count_documents({'ministry':a})
        subtitle2.append(search_data3)
    

    
    # Creating dataset
    # cars = ['AUDI', 'BMW', 'FORD',
    #         'TESLA', 'JAGUAR', 'MERCEDES']

    cars = subtitle
    
    data = subtitle2

    

    
    
    # Creating explode data
    explode = (0.1, 0.0)
    
    # Creating color parameters
    colors = ( "orange", "cyan","blue","yellow")
    
    # Wedge properties
    wp = { 'linewidth' : 1, 'edgecolor' : "green" }
    
    # Creating autocpt arguments
    def func(pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)
    
    # Creating plot
    fig, ax = plt.subplots(figsize =(10, 7))
    wedges, texts, autotexts = ax.pie(data,
                                    autopct = lambda pct: func(pct, data),
                                    
                                    labels = cars,
                                    shadow = True,
                                    colors = colors,
                                    startangle = 90,
                                    wedgeprops = wp,
                                    textprops = dict(color ="magenta"))
    
    # Adding legend
    ax.legend(wedges, cars,
            title ="Ministry",
            loc ="center left",
            bbox_to_anchor =(1, 0, 0.5, 1))
    
    plt.setp(autotexts, size = 11, weight ="bold")
    ax.set_title("Arise Church Member's Data Chart")
    
    # show plot
    plt.show()
def testing_array():

    arr =['jerome','alson']
    for i in arr:
        print(tabulate(i[0], headers =['Name'], tablefmt='psql'))
        



# testing_array()
# call_array()
# testing_piechart()
# testing()
# insert_login_()
log_in()
# list_ministry()
# church_ministry()