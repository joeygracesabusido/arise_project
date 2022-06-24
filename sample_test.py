from sample import Database

Database.initialize()

@staticmethod
def search_one():
    data = Database.find(collection='admin_login')
    for i in data:
        fullname = i['fullname']
        print(fullname)

search_one()