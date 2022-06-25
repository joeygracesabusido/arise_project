from database import Database
from datetime import datetime

Database.initialize()

# agg_result= collection.count_documents(
#         { '$and': [ {'created': {'$gte':date_time_obj,'$lte':dateToday}},
#             {'members_id':members_ID_time.get()} ] } )

@staticmethod
def list_churchMinistry():
    """
    This function is for 
    calling the List of Church ministry
    """
    date_time_str = input('Enter Date: ')
    timeNow = ('00:00:00')
    date_time_str2 = date_time_str + ' ' + timeNow
    date_time_obj = datetime.strptime(date_time_str2, '%Y-%m-%d %H:%M:%S')
    dateToday = datetime.now()
    data = Database.find_all(collection='church_ministry')
    

    subtitle=[]
    for value in data:
        subtitle.append(value['ministry'])

    
    search_data2 = Database.find_all(collection='church_ministry')
    a = ''
    
    subtitle2=[]
    for i in search_data2:
        a = i['ministry']

        search_data3 = Database.search_count(collection='attendance', 
                                query={ '$and': [ {'created': {'$gte':date_time_obj,'$lte':dateToday}},
                                        {'ministry':{
                                            '$regex': a,
                                            '$options': 'i' 
                                            }}
                                            ] } 
                                            )
        subtitle2.append(search_data3)
    # print(subtitle)
    # print(subtitle2)
        

        # dataSearch3 = db['members_detail']

        # search_data3= dataSearch3.count_documents({'ministry':a})
        # subtitle2.append(search_data3)
def testCount():
    """
    This function is for 
    testing count
    """ 
    date_time_str = input('Enter Date: ')
    timeNow = ('00:00:00')
    date_time_str2 = date_time_str + ' ' + timeNow
    date_time_obj = datetime.strptime(date_time_str2, '%Y-%m-%d %H:%M:%S')
    dateToday = datetime.now()

    search_data3 = Database.search_count(collection='attendance', 
                                query={'created': {'$gte':date_time_obj,'$lte':dateToday}})
                                       
    print(search_data3)

# testCount()
list_churchMinistry()


