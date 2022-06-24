from sample import Database

Database.initialize()

@staticmethod
def search_all():
    data = Database.find_all(collection='admin_login')
    for i in data:
        fullname = i['fullname']
        print(fullname)
        print(i)

def search_one():
    """
    This function is for
    searching one person
    """

    query_item = input('Enter Search Name:  ')
    data = Database.find_one(collection='admin_login', query={'fullname':{
                                    '$regex': query_item,
                                     '$options': 'i' 
                                     }})
    for i in data:
        print(i)

def update_approval():
    """
    This function is for
    updating approval of user
    """
    query_item = input('Enter Name:  ')
    status_approved = input('Enter approved or for approval: ')

    data = Database.update_approval(collection='admin_login', query={'fullname':{
                                    '$regex': query_item,
                                     '$options': 'i' 
                                     }},
                                     newValue={ "$set": { 
                                                'status': status_approved 
                                            }           
                                        }
                                     )
    
    search_all()

# update_approval()
search_all()
# search_one()