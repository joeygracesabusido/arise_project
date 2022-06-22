from datetime import date
from datetime import timedelta, date
import datetime



date1 = input('Enter Date from: ')
time_now = '00:00:00'

dateFrom = date1 
date2 = datetime.datetime.strptime(dateFrom, "%Y-%m-%d")
number_of_days = int(input('Enter number of days: '))


dueDate = date2 + timedelta(days=number_of_days)
print(dueDate)