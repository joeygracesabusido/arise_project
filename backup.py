from database import Database
import xlsxwriter
from os import startfile

Database.initialize()

@staticmethod
def backup():
    """
    This function is for 
    backup
    """
    workbook = xlsxwriter.Workbook("membersDetail.xlsx")
    worksheet = workbook.add_worksheet('members')
    worksheet.write('A1', 'ID')
    worksheet.write('B1', 'Last Name')
    worksheet.write('C1', 'First Name')
    worksheet.write('D1', 'Address')
    worksheet.write('E1', 'BirthDay')
    worksheet.write('F1', 'age')
    worksheet.write('G1', 'Ministry')
    worksheet.write('H1', 'Contact No')
   
    
   
   
    rowIndex = 2
    data = Database.find_all(collection='members_detail')
    for i in data:
        members_id = i['members_id']
        lname = i['lname']
        fname = i['fname']
        address = i['address']
        birthday = i['birthday']
        age = i['age']
        ministry = i['ministry']
        contact_num = i['contact_num']
    
    
        worksheet.write('A' + str(rowIndex),members_id)
        worksheet.write('B' + str(rowIndex),lname)
        worksheet.write('C' + str(rowIndex),fname)
        worksheet.write('D' + str(rowIndex),address)
        worksheet.write('E' + str(rowIndex),birthday)
        worksheet.write('F' + str(rowIndex),age)
        worksheet.write('G' + str(rowIndex),ministry)
        worksheet.write('H' + str(rowIndex),contact_num)
      
       
       
        
       
        
        rowIndex += 1

    workbook.close()
    print('JRS', 'Data has been exported')    

    # from os import startfile
    startfile("membersDetail.xlsx")

