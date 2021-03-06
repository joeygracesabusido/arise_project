from distutils import command
from email.mime import text
from importlib.resources import contents
from lib2to3.pgen2.token import ENDMARKER
from tkinter import *
import csv
# from types import NoneType
import xdrlib
# from types import NoneType
from PIL import Image, ImageTk
import PIL.Image
import tkinter.ttk as ttk
import tkinter.messagebox as tkMessageBox
import datetime as dt
from numpy import True_, true_divide
from tkcalendar import DateEntry
from tkcalendar import DateEntry as TkcDateEntry
import tkinter as tk
from tkinter import scrolledtext
import time
import datetime
import tkinter.messagebox as tkMessageBox
from tkinter import messagebox
from reportlab.pdfgen.canvas import Canvas
from PollyReports import *
from os import startfile
import xlsxwriter

from matplotlib import pyplot as plt

# from docx import Document
# from docx.shared import Inches

from datetime import date, timedelta
from datetime import datetime

from fpdf import FPDF

#from PIL import ImageTk, Image as PILImage
#from payroll import selectTransaction
import babel.numbers

from tkinter.scrolledtext import ScrolledText

from pymongo import MongoClient
import pandas as pd
import re
# from datetime import timedelta 

from matplotlib import pyplot as plt
import numpy as np

# this is for classes function
# from chart_of_account import testCoa




from bson.objectid import ObjectId
import dateutil.parser
import pymongo

import certifi
ca = certifi.where()

# import registration

client = pymongo.MongoClient(f"mongodb+srv://joeysabusido:genesis11@cluster0.r76lv.mongodb.net/?retryWrites=true&w=majority", tlsCAFile=ca)

db = client.arise_church





root = Tk()
root.title("JRS SYSTEM")

width = 750
height = 500
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)
root.geometry("%dx%d+%d+%d" % (width, height, x, y))
root.resizable(0, 0)
root.config(bg="cyan")

#load = Image.open("image\login.png").convert("RGB")
load = PIL.Image.open("image\login.png")
load =load.resize((150, 125), PIL.Image.ANTIALIAS)
logo_icon = ImageTk.PhotoImage(load)


def clearFrame():
    # destroy all widgets from frame
    for widget in MidViewForm9.winfo_children():
        widget.destroy()

    # this will clear frame and frame will be empty
    # if you want to hide the empty panel then
    MidViewForm9.pack_forget()

# ==========================================Back up Data ===============================================
def backuData():
    """
    This function is for 
    Back up Data to excel file
    """  
    from backup import backup
    # from membersPiechart import list_churchMinistry
    backup()

    # post = list_churchMinistry()
    # print(post)
#===========================================Report Frame=================================================
def members_attendanceComposition_Function():
    """
    This is for function 
    for attendance Chart
    """
    from database import Database
    Database.initialize()

    
    date_time_str2 = dateSearch_attendanceChart.get()
    timeNow = ('00:00:00')
    # date_time_str3 =date_time_str2 + '' +timeNow
    # date_time_obj_from = datetime.strptime(date_time_str2, '%Y-%m-%d')
    date_time_obj = datetime.strptime(date_time_str2, '%Y-%m-%d')

    dateToday1 = dateSearchTo_attendanceChart.get()
    dateToday = datetime.strptime(dateToday1, '%Y-%m-%d')


    data = Database.find_all(collection='church_ministry')# search for all data in church_ministry table
    

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
    
    ministry = subtitle
    
    data = subtitle2


    
    # Creating explode data
    explode = (0.1, 0.0)
    
    # Creating color parameters
    colors = ( "orange", "cyan","blue","yellow",
                "green","brown","red")
    
    # Wedge properties
    wp = { 'linewidth' : 1, 'edgecolor' : "green" }
    
    # Creating autocpt arguments
    def func(pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)
    
    # Creating plot
    fig, ax = plt.subplots(figsize =(8, 5))
    wedges, texts, autotexts = ax.pie(data,
                                    autopct = lambda pct: func(pct, data),
                                    
                                    labels = ministry,
                                    shadow = True,
                                    colors = colors,
                                    startangle = 90,
                                    wedgeprops = wp,
                                    textprops = dict(color ="black"))
    
    # Adding legend
    ax.legend(wedges, ministry,
            title ="Ministry",
            loc ="center left",
            bbox_to_anchor =(1, 0, 0.5, 1))
    
    plt.setp(autotexts, size = 10, weight ="bold")
    ax.set_title("Arise Church Attendance's Data Chart")
    
    # show plot
    plt.show()


def members_attendanceComposition_frame():
    """
    This function is for 
    chart of attendance
    """
    chart_attendaceChartframe = Frame(MidViewForm9, width=950, height=400, bd=2, bg='gray', relief=SOLID)
    chart_attendaceChartframe.place(x=20, y=8)


    absent_date_label = Label(chart_attendaceChartframe, text='From',
                        width=13, height=1, bg='yellow', fg='black',
                        font=('Arial', 10), anchor='center')
    absent_date_label.place(x=150, y=30)



    global dateSearch_attendanceChart
    dateSearch_attendanceChart = DateEntry(chart_attendaceChartframe, width=15, background='darkblue',
                                  date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    dateSearch_attendanceChart.place(x=270, y=30)
    dateSearch_attendanceChart.configure(justify='center')

    absent_date_label_to = Label(chart_attendaceChartframe, text='From',
                        width=13, height=1, bg='yellow', fg='black',
                        font=('Arial', 10), anchor='center')
    absent_date_label_to.place(x=400, y=30)

    global dateSearchTo_attendanceChart
    dateSearchTo_attendanceChart = DateEntry(chart_attendaceChartframe, width=15, background='darkblue',
                                  date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    dateSearchTo_attendanceChart.place(x=530, y=30)
    dateSearchTo_attendanceChart.configure(justify='center')

    btn_search_attendanceChart = Button(chart_attendaceChartframe, text='Search', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=7, height=1,
                              command=members_attendanceComposition_Function)
    btn_search_attendanceChart.place(x=650, y=30)
    btn_search_attendanceChart.bind('<Return>', members_attendanceComposition_Function)

def birthday_list_function():
    """
    This function is
    calling birthday List for the Month 
    """
    bdayList_frame_listbox.delete(0, END)
    collection = db['members_detail']
   
    
    agg_result = collection.find().sort('lname', pymongo.ASCENDING)
    dateNow = datetime.now()
    
    # print(dateNow.month)
    
    for i in agg_result:
        bday = i['birthday']
        datem = datetime.strptime(bday, "%Y-%m-%d")
        
        if datem.month == dateNow.month:
            bdayList = i['fname']+ ' ' +i['lname']+ ' ' +i['birthday']
            bdayList_frame_listbox.insert(END,(bdayList))
            
def birthday_list_frame():
    """
    This function is for
    Birth day List frame
    """
    bdayList_frame = Frame(MidViewForm9, width=930, height=400, bd=2, bg='gray', relief=SOLID)
    bdayList_frame.place(x=20, y=8)

    trans_label = Label(bdayList_frame, text='Greeting!!! HAPPY BIRTH DAY FROM ARISE FAMILY',
                        width=50, height=1, bg='pink', fg='black',
                          font=('Arial', 15), anchor='center')
    trans_label.place(x=150, y=2)

    global bdayList_frame_listbox
    bdayList_frame_listbox = tk.Listbox(bdayList_frame,
                                  width=50, height=10, bg='darkblue', fg='white', font=('courier', 15))
    bdayList_frame_listbox.place(x=150, y=70)
    # bdayList_frame_listbox.bind("<KeyRelease>",absent_members_btn)
    
    birthday_list_function()
    
def absent_members_btn():
    """
    this function is for searching for 
    absent with buttons
    """
    absent_listbox.delete(0, END)
    datefrom = dateSearch_absent.get()
    date_time_obj_from = datetime.strptime(datefrom, '%Y-%m-%d')
    
    dateto = dateSearchTo.get()
    date_time_obj_to = datetime.strptime(dateto, '%Y-%m-%d')

    dataSearch2 = db['attendance']
    search_data2 = dataSearch2.find({'created': {'$gte':date_time_obj_from, '$lte':date_time_obj_to}})

    
    
    subtitle1=[]
    for i in search_data2:
        a = i['members_id']+ ' ' +i['fname']+' ' +i['lname']
        
        subtitle1.append(a)
    


    dataSearch3 = db['members_detail']
    search_data3= dataSearch3.find()
    # search_data3= dataSearch3.find({'members_id': { '$ne': a } })
    subtitle2=[]
    for i in search_data3:
        b = i['members_id']+ ' ' +i['fname']+' ' +i['lname']
        subtitle2.append(b)
    
    # this is how to compare the list and give the result of the comparison
    res = [x for x in subtitle1 + subtitle2 if x not in subtitle1 or x not in subtitle2]
    count =0 
    for i in res:
        count+=1
        absent = str(count) + ' ' + i
        # absent_listbox.delete(0, END)
        absent_listbox.insert(END,(absent))
        absent_listbox.bind("<KeyRelease>",absent_members_btn)


def absent_members():
    """
    this function is for absent
    members
    """
    datefrom = dateSearch_absent.get()
    date_time_obj_from = datetime.strptime(datefrom, '%Y-%m-%d')
    
    dateto = datetime.now()

    dataSearch2 = db['attendance']
    search_data2 = dataSearch2.find({'created': {'$gte':date_time_obj_from, '$lte':dateto}})

    
    
    subtitle1=[]
    for i in search_data2:
        a = i['members_id']+ ' ' +i['fname']+' ' +i['lname']
        
        subtitle1.append(a)
    


    dataSearch3 = db['members_detail']
    search_data3= dataSearch3.find()
    # search_data3= dataSearch3.find({'members_id': { '$ne': a } })
    subtitle2=[]
    for i in search_data3:
        b = i['members_id']+ ' ' +i['fname']+' ' +i['lname']
        subtitle2.append(b)
    

    res = [x for x in subtitle1 + subtitle2 if x not in subtitle1 or x not in subtitle2]
    count =0 
    for i in res:
        count+=1
        absent = str(count) + ' ' + i

        # absent_listbox.delete(0, END)
        absent_listbox.insert(END,(absent))
    
    # for i in res:
        
        # absent_listbox.insert(END, absent)
        # absent_listbox.insert(END, (i))
    
def absent_members_frame():
    """
    This function is for absent member frame
    """
    
    absent_data_frame = Frame(MidViewForm9, width=950, height=400, bd=2, bg='gray', relief=SOLID)
    absent_data_frame.place(x=20, y=8)


    

    global absent_listbox
    absent_listbox = tk.Listbox(absent_data_frame,
                                  width=140, height=18, bg='darkblue', fg='white', font=('courier', 10))
    absent_listbox.place(x=150, y=70)
    absent_listbox.bind("<KeyRelease>",absent_members_btn)


    absent_date_label = Label(absent_data_frame, text='From',
                        width=13, height=1, bg='yellow', fg='black',
                        font=('Arial', 10), anchor='center')
    absent_date_label.place(x=150, y=30)



    global dateSearch_absent
    dateSearch_absent = DateEntry(absent_data_frame, width=15, background='darkblue',
                                  date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    dateSearch_absent.place(x=270, y=30)
    dateSearch_absent.configure(justify='center')

    absent_date_label_to = Label(absent_data_frame, text='From',
                        width=13, height=1, bg='yellow', fg='black',
                        font=('Arial', 10), anchor='center')
    absent_date_label_to.place(x=400, y=30)

    global dateSearchTo
    dateSearchTo = DateEntry(absent_data_frame, width=15, background='darkblue',
                                  date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    dateSearchTo.place(x=530, y=30)
    dateSearchTo.configure(justify='center')

    btn_search = Button(absent_data_frame, text='Search', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=7, height=1,command=absent_members_btn)
    btn_search.place(x=650, y=30)
    btn_search.bind('<Return>', absent_listbox)

    absent_members()
    
def graph_attendance():

    """
    This function is for
    graphical representation
    of church attendance
    """ 

    dataSearch3 = db['attendance']
   
    agg_result = dataSearch3.find()

    subtitle2=[]
    for i in agg_result:
        date1 = i['created']
        # datem = datetime.strptime(date1, "%Y-%m-%d")
        datem = (date1.strftime('%Y-%m-%d'))
        subtitle2.append(datem)
    # res = Counter(subtitle2)
    result = dict((i, subtitle2.count(i)) for i in subtitle2) # count of attendance tru looping ofdate
    keys = result.keys()

    number_of_attendae = result.values()
    date1 =[]
    for i in keys:
        date1.append(i)
    
    
    number2 = []
    for x in number_of_attendae:
        number2.append(x)

   
    x = date1 # group of date for attendance
    y = number2 # number of attendae in list data

    plt.plot(x,y)
    plt.title("Attendance Graph per Services")
    plt.xlabel("Dates")
    plt.ylabel("Number of Attendae")
    plt.show()


def membersAttendance_pieChart():
    """
    This function is for
    pie chart of members Attendance
    """

    


def report_piechart_members_Data():
    """
    this function is to test pie chart

    """
    dataSearch = db['church_ministry']
    search_data = dataSearch.find()
   
         
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
    
    

    cars = subtitle
    
    data = subtitle2


    
    # Creating explode data
    explode = (0.1, 0.0)
    
    # Creating color parameters
    colors = ( "orange", "cyan","blue","yellow",
                "green","brown","red")
    
    # Wedge properties
    wp = { 'linewidth' : 1, 'edgecolor' : "green" }
    
    # Creating autocpt arguments
    def func(pct, allvalues):
        absolute = int(pct / 100.*np.sum(allvalues))
        return "{:.1f}%\n({:d} g)".format(pct, absolute)
    
    # Creating plot
    fig, ax = plt.subplots(figsize =(9, 5))
    wedges, texts, autotexts = ax.pie(data,
                                    autopct = lambda pct: func(pct, data),
                                    
                                    labels = cars,
                                    shadow = True,
                                    colors = colors,
                                    startangle = 90,
                                    wedgeprops = wp,
                                    textprops = dict(color ="black"))
    
    # Adding legend
    ax.legend(wedges, cars,
            title ="Ministry",
            loc ="center left",
            bbox_to_anchor =(1, 0, 0.5, 1))
    
    plt.setp(autotexts, size = 11, weight ="bold")
    ax.set_title("Arise Church Member's Data Chart")
    
    # show plot
    plt.show()

def perMinistryAttendance():
    """
    This function
    is for querying of per ministry attendance

    """
    dataSearch = db['attendance']

    datefrom = dateSearch.get()
    date_time_obj_from = datetime.strptime(datefrom, '%Y-%m-%d')
    
    dateto = dateSearchTo_attendanceList.get()
    date_time_obj_to = datetime.strptime(dateto, '%Y-%m-%d')
    
    search_data = dataSearch.find({'created': {'$gte':date_time_obj_from, '$lte':date_time_obj_to}}).sort('created', pymongo.ASCENDING) 

    subtitle2=[]
    for i in search_data:
        a = i['ministry']
        

        dataSearch3 = db['attendance']

        search_data3= dataSearch3.count_documents({'ministry':a})
        subtitle2.append(search_data3)
    for z in subtitle2:
        print(z)
def attendance_list_function():
    
    """
    this function is for
    calling the Members List
    """
    membersList_attendance_treeview.delete(*membersList_attendance_treeview.get_children())
    return attendance_list_btn()


def attendance_list_btn():
    """
    This function is for
    attendance list
    """
    
    dataSearch = db['attendance']

    datefrom = dateSearch.get()
    date_time_obj_from = datetime.strptime(datefrom, '%Y-%m-%d')
    
    dateto = dateSearchTo_attendanceList.get()
    date_time_obj_to = datetime.strptime(dateto, '%Y-%m-%d')
    
    search_data = dataSearch.find({'created': {'$gte':date_time_obj_from, '$lte':date_time_obj_to}}).sort('created', pymongo.ASCENDING)

    members ={}
    count = 0
    for row in search_data:
        count+=1
       
        data = {
            'members_id': row['members_id'],
            'lname': row['lname'],
            'fname': row['fname'],
            'ministry': row['ministry'],
            'count': count,
        }
        
        members.update(data)
        
        membersList_attendance_treeview.insert('', 'end', values=(members['count'],members['members_id'],members['lname'],
                                members['fname'],members['ministry']))

        # perMinistryAttendance()
def attendance_list():
    """
    This function is for
    attendance list
    """
    
    dataSearch = db['attendance']

    datefrom = dateSearch.get()
    date_time_obj_from = datetime.strptime(datefrom, '%Y-%m-%d')
    
    dateto = datetime.now()
    
    
    search_data = dataSearch.find({'created': {'$gte':date_time_obj_from, '$lte':dateto}}).sort('created', pymongo.ASCENDING)

    members ={}
    count = 0
    for row in search_data:
        count+=1
       
        data = {
            'members_id': row['members_id'],
            'lname': row['lname'],
            'fname': row['fname'],
            'ministry': row['ministry'],
            'count': count,
        }
        
        members.update(data)
        
        membersList_attendance_treeview.insert('', 'end', values=(members['count'],members['members_id'],members['lname'],
                                members['fname'],members['ministry']))
 
    
def attendance_list_frame():
    """
    This function is for
    list of Attendance
    """
    
    members_attendance_list_frame = Frame(MidViewForm9, width=950, height=400, bd=2, bg='gray', relief=SOLID)
    members_attendance_list_frame.place(x=20, y=8)
    
    trans_label = Label(members_attendance_list_frame, text='LIST OF PRESENT',
                        width=35, height=1, bg='pink', fg='black',
                          font=('Arial', 15), anchor='center')
    trans_label.place(x=250, y=2)
    
    global dateSearch
    dateSearch = DateEntry(members_attendance_list_frame, width=15, background='darkblue',
                                  date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    dateSearch.place(x=10, y=50)
    dateSearch.configure(justify='center')


    absent_date_label_to = Label(members_attendance_list_frame, text='To',
                        width=13, height=1, bg='yellow', fg='black',
                        font=('Arial', 10), anchor='center')
    absent_date_label_to.place(x=10, y=80)

    global dateSearchTo_attendanceList
    dateSearchTo_attendanceList = DateEntry(members_attendance_list_frame, width=15, background='darkblue',
                                  date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    dateSearchTo_attendanceList.place(x=10, y=120)
    dateSearchTo_attendanceList.configure(justify='center')
    
    btn_search = Button(members_attendance_list_frame, text='Search', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=7, height=1,command=attendance_list_function)
    btn_search.place(x=10, y=180)


    # global transacID
    # transacID= Entry(members_attendance_list_frame, width=15, font=('Arial', 12))
    # transacID.place(x=110, y=55)
    
    
    memberslist_attendance_Form = Frame(members_attendance_list_frame, width=600, height=10)
    memberslist_attendance_Form.place(x=250, y=30)

    style = ttk.Style(members_attendance_list_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="cyan",
                    rowheight=15,
                    fieldbackground="yellow")
   
    
    
    global membersList_attendance_treeview
    scrollbarx = Scrollbar(memberslist_attendance_Form, orient=HORIZONTAL)
    scrollbary = Scrollbar(memberslist_attendance_Form, orient=VERTICAL)
    
    membersList_attendance_treeview = ttk.Treeview(memberslist_attendance_Form,
                                             columns=('Count','ID','LNAME', "FNAME","MINISTRY",
                                              ),
                                             selectmode="extended", height=20, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=membersList_attendance_treeview.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=membersList_attendance_treeview.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    membersList_attendance_treeview.heading('Count', text="Count", anchor=CENTER)
    membersList_attendance_treeview.heading('ID', text="ID", anchor=CENTER)
    membersList_attendance_treeview.heading('LNAME', text="Last Name", anchor=CENTER)
    membersList_attendance_treeview.heading('FNAME', text="First Name", anchor=CENTER)
    membersList_attendance_treeview.heading('MINISTRY', text="Ministry", anchor=CENTER)
    


    membersList_attendance_treeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    membersList_attendance_treeview.column('#1', stretch=NO, minwidth=0, width=70, anchor='e')
    membersList_attendance_treeview.column('#2', stretch=NO, minwidth=0, width=150, anchor='e')
    membersList_attendance_treeview.column('#3', stretch=NO, minwidth=0, width=150, anchor='e')
    membersList_attendance_treeview.column('#4', stretch=NO, minwidth=0, width=150, anchor='e')
    membersList_attendance_treeview.column('#5', stretch=NO, minwidth=0, width=150, anchor='e')
    

    membersList_attendance_treeview.pack()
    attendance_list()
#=========================================this is for accounting frame==========================================


def coa_list_value():
    """
    This function is for
    coa list
    """
    dataSearch = db['chartOFaccount'] 
    # agg_result = dataSearch.find()
    agg_result = dataSearch.find().sort('chart_of_account', pymongo.ASCENDING)

    data = []
    for x in agg_result:
        data1 = x['chart_of_account'] + ' ' + x['category']
        data.append(data1)
    return data

def coa_list():

    """
    This function is for 
    testing list coa from importation
    """
    from chart_of_account import test_coa
    collection = db['chartOFaccount']
    query = collection.find()

    listCOA = {}
    Test_list = ''
    count = 0
    for i in query:
        
        # listCOA.update({len(listCOA)+1:{
                
        #         'chart_of_account': i['chart_of_account'],
        #         'category': i['category'],
                
        #     }})
        data = {
                
                'chart_of_account': i['chart_of_account'],
                'category': i['category'],
                
            }
        
        listCOA.update(data)
        Test_list =test_coa(listCOA)  

        Test_list.list_chart_of_account()

        # coa_listbox.delete(0, END)
        coa_listbox.insert(END,(Test_list.list_chart_of_account()))




def insert_coa():
    """
    This function is for inserting
    chart of account
    """
    # from pythonClass import Person

    from chart_of_account import SaveCoa

   

    
    coa_listbox.delete(0, END)
    Chart_of_account = chart_of_account_insert_entry.get()
    Category = category_coa_entry.get()

    chartOfAccount = SaveCoa(Chart_of_account,Category)

    chartOfAccount.insert_chartofAccount()
    
    messagebox.showinfo('JRS','Your chart of account Has been Save')
    coa_list()

    chart_of_account_insert_entry.delete(0, END)
    category_coa_entry.delete(0, END)




def chart_of_account():
    """
    This function is for 
    inserting chart of account
    """
   
    
    chart_of_account_frame = Frame(MidViewForm9, width=950, height=400, bd=2, bg='gray', relief=SOLID)
    chart_of_account_frame.place(x=20, y=8)

    global coa_listbox
    coa_listbox = tk.Listbox(chart_of_account_frame,
                                  width=50, height=18, bg='darkblue', fg='white', font=('courier', 10))
    coa_listbox.place(x=450, y=70)
    coa_listbox.bind("<KeyRelease>",absent_members_btn)

    chart_of_account_lbl = Label(chart_of_account_frame, text='Chart of account',
                        width=15, height=1, bg='yellow', fg='black',
                        font=('Arial', 10), anchor='center')
    chart_of_account_lbl.place(x=10, y=80)

    global chart_of_account_insert_entry
    chart_of_account_insert_entry = Entry(chart_of_account_frame, width=20, font=('Arial', 11))
    chart_of_account_insert_entry.place(x=150, y=85)

    chart_of_account_lbl = Label(chart_of_account_frame, text='Account Category',
                        width=15, height=1, bg='yellow', fg='black',
                        font=('Arial', 10), anchor='center')
    chart_of_account_lbl.place(x=10, y=115)

    global category_coa_entry
    category_coa_entry = ttk.Combobox(chart_of_account_frame, width=13,font=('Arial', 11))
    category_coa_entry['values'] = ['Income','Expense']
    category_coa_entry.place(x=150, y=115)

    btn_save = Button(chart_of_account_frame, text='Save', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=7, height=1,command=insert_coa)
    btn_save.place(x=10, y=140)

    coa_list()

def delete_journalEntry():
    """
    This function is for 
    deleting journal entry
    """
    dataSearch = db['journal_entry']
    query = {'_id': ObjectId(search_id_entry.get())}

    if search_id_entry =='':
        messagebox.showinfo('JRS', 'Please fill up TRans id for delete Transaction')
    else:
        result = tkMessageBox.askquestion('JRS','Are you sure you want to Update?',icon="warning")
        if result == 'yes':
            x = dataSearch.delete_one(query)
            messagebox.showinfo('JRS', 'Selected Record has been deleted')
            view_journal_entry_treeview()

def select_record_treeview_journalEntry():
    """
    this function is for
    selecting record from
    treeview
    """
    
    particular_journale_entry.delete('1.0',END)
    amount_entry.delete(0, END)
    chartOfAccount_list_entry.delete(0, END)


    selected = accounting_search_treeview.focus()
    values = accounting_search_treeview.item(selected)
    selectedItems = values['values']
    


    dataSearch = db['journal_entry']
    query = {'_id': ObjectId(selectedItems[0])}
    try:
       
        
        for x in dataSearch.find(query):
            
            id_num = x['_id']
            date_entry = x['date']
            chartofAccount = x['chart_of_account']
            amount = x['amount']
            particular = x['particular']
            
            
            date_journal_entry.insert(0, date_entry)
            chartOfAccount_list_entry.insert(0, chartofAccount)
            amount_entry.insert(0, amount)
            particular_journale_entry.insert('1.0', particular)

            search_id_entry.delete(0,END)
            search_id_entry.insert(0,id_num)
            

    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")

def view_journal_entry_treeview():
    
    """
    this function is for
    button to display the list
    of supplier
    """
    
    accounting_search_treeview.delete(*accounting_search_treeview.get_children())
    return view_journal_entry()

def view_journal_entry():
    """
    This function is for 
    accounting treeview
    """
    dataSearch = db['journal_entry']
    # query = {'customerID':customerID_entry.get() }
    try:
        count =0
        for x in dataSearch.find():
            count+=1
            id_num = x['_id']
            date_search = x['date']
            chart_of_account = x['chart_of_account']
            amount = x['amount']
            amount2 = '{:,.2f}'.format(amount)
            particular = x['particular']
            
            accounting_search_treeview.insert('', 'end', values=(id_num,count,date_search,
                                    chart_of_account,amount2,particular))

            
    except Exception as ex:
        messagebox.showerror("Error", f"Error due to :{str(ex)}")



def insert_journal_entry():
    """
    This function is for 
    Inserting Data to journal Entry Database
    """

    from chart_of_account import InsertJournal

    date_entry = date_journal_entry.get()
    chart_ofAccount = chartOfAccount_list_entry.get()
    amount = float(amount_entry.get())
    particular = particular_journale_entry.get('1.0', 'end-1c')

    if date_entry == '' or chart_ofAccount == '' or amount == '' or particular == '':
        messagebox.showinfo('JRS','Please fill up blank fields')
    else:
        insert_entry = InsertJournal(date_entry,chart_ofAccount,amount,particular)
        messagebox.showinfo('JRS','Your Data has been save')
        insert_entry.insert_journal()
        view_journal_entry_treeview()
        

        particular_journale_entry.delete('1.0',END)
        amount_entry.delete(0, END)
        chartOfAccount_list_entry.delete(0, END)
def journal_entry():
    """
    This function is for
    Journal Entry
    """  
    from chart_of_account import test_coa
    accounting_frame = Frame(MidViewForm9, width=950, height=400, bd=2, bg='gray', relief=SOLID)
    accounting_frame.place(x=20, y=8)
    
    trans_label = Label(accounting_frame, text='LIST OF PRESENT',
                        width=35, height=1, bg='pink', fg='black',
                          font=('Arial', 15), anchor='center')
    trans_label.place(x=250, y=2)

    chartOfAccount_list_label = Label(accounting_frame, text='TRans Date:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    chartOfAccount_list_label.place(x=10, y=50)
    
    global date_journal_entry
    date_journal_entry = DateEntry(accounting_frame, width=15, background='darkblue',
                                  date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    date_journal_entry.place(x=150, y=50)
    date_journal_entry.configure(justify='center')


    chartOfAccount_list_label = Label(accounting_frame, text='Chart of Account:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    chartOfAccount_list_label.place(x=10, y=80)

   
    global chartOfAccount_list_entry
    chartOfAccount_list_entry = ttk.Combobox(accounting_frame, width=15)
    chartOfAccount_list_entry['values'] = coa_list_value()
    chartOfAccount_list_entry.place(x=150, y=80)

    chartOfAccount_list_label = Label(accounting_frame, text='Amount:', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    chartOfAccount_list_label.place(x=10, y=110)

    global amount_entry
    amount_entry = Entry(accounting_frame, width=20, font=('Arial', 11))
    amount_entry.place(x=150, y=110)

    add_reg_label = Label(accounting_frame, text='Particular:', width=14, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    add_reg_label.place(x=10, y=140)

    global particular_journale_entry
    particular_journale_entry = scrolledtext.ScrolledText(accounting_frame,
                                                          wrap=tk.WORD,
                                                          width=20,
                                                          height=3,
                                                          font=("Arial",
                                                                10))
    particular_journale_entry.place(x=150, y=140)

    
   


    chartOfAccount_list_label = Label(accounting_frame, text='Trans ID', 
                                            width=14, height=1, bg='yellow', fg='black',
                                             font=('Arial', 10), anchor='e')
    chartOfAccount_list_label.place(x=10, y=235)

    global search_id_entry
    search_id_entry = Entry(accounting_frame, width=20, font=('Arial', 11))
    search_id_entry.place(x=150, y=235)

    

    btn_journalSave = Button(accounting_frame, text='Save', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=7, height=1,command=insert_journal_entry)
    btn_journalSave.place(x=10, y=200)


    btn_search_func = Button(accounting_frame, text='Selected Value', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1,
                              command=select_record_treeview_journalEntry)
    btn_search_func.place(x=800, y=10)

    btn_search_func = Button(accounting_frame, text='Delete', bd=2, bg='red', fg='white',
                              font=('arial', 10), width=10, height=1,
                              command=delete_journalEntry)
    btn_search_func.place(x=150, y=200)

    
    
    
    accounting_search_treeviewForm = Frame(accounting_frame, width=600, height=10)
    accounting_search_treeviewForm.place(x=350, y=30)

    style = ttk.Style(accounting_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="white",
                    foreground="black",
                    rowheight=15,
                    fieldbackground="yellow")
   
    
    
    global accounting_search_treeview
    scrollbarx = Scrollbar(accounting_search_treeviewForm, orient=HORIZONTAL)
    scrollbary = Scrollbar(accounting_search_treeviewForm, orient=VERTICAL)
    
    accounting_search_treeview = ttk.Treeview(accounting_search_treeviewForm,
                                             columns=('ID','Count','Date','ChartofAccount', "Particular",
                                             "Amount",
                                              ),
                                             selectmode="extended", height=20, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=accounting_search_treeview.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=accounting_search_treeview.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    accounting_search_treeview.heading('ID', text="ID", anchor=CENTER)
    accounting_search_treeview.heading('Count', text="Count", anchor=CENTER)
    accounting_search_treeview.heading('Date', text="Date", anchor=CENTER)
    accounting_search_treeview.heading('ChartofAccount', text="Chart of Account", anchor=CENTER)
    accounting_search_treeview.heading('Particular', text="Particular", anchor=CENTER)
    accounting_search_treeview.heading('Amount', text="Amount", anchor=CENTER)
    


    accounting_search_treeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    accounting_search_treeview.column('#1', stretch=NO, minwidth=0, width=30, anchor='e')
    accounting_search_treeview.column('#2', stretch=NO, minwidth=0, width=70, anchor='e')
    accounting_search_treeview.column('#3', stretch=NO, minwidth=0, width=100, anchor='e')
    accounting_search_treeview.column('#4', stretch=NO, minwidth=0, width=100, anchor='e')
    accounting_search_treeview.column('#5', stretch=NO, minwidth=0, width=100, anchor='e')
    accounting_search_treeview.column('#5', stretch=NO, minwidth=0, width=100, anchor='e')
    

    accounting_search_treeview.pack()
    view_journal_entry_treeview()
    



#===========================================Attendance Frame=====================================
def insert_attendance():
    """
    This function is to insert attendance
    """


    
    collection = db['attendance']
    datefrom = dateSearch_timeIn.get()
    timeNow = ('00:00:00')
    date_time_str2 = datefrom + ' ' + timeNow
    date_time_obj = datetime.strptime(date_time_str2, '%Y-%m-%d %H:%M:%S')
    dateToday = datetime.now()

    agg_result= collection.count_documents(
        { '$and': [ {'created': {'$gte':date_time_obj,'$lte':dateToday}},
            {'members_id':members_ID_time.get()} ] } )
   
    if agg_result > 0:
            messagebox.showinfo('JRS','Members Has been already time in')
            
        
    else:   
        dataInsert = {
            'members_id': members_ID_time.get(),
            'lname': last_name_member_reg_time.get(),
            'fname': first_name_member_reg_time.get(),
            'ministry':ministry_reg_entry_time.get(),
            'created':datetime.now()
            
        }
        
        try:
            collection.insert_one(dataInsert)
            
            messagebox.showinfo('JRS','Your Attendance Has been Save')
            attendance_list_frame()
            last_name_member_reg_time.delete(0, END)
            first_name_member_reg_time.delete(0, END)
            ministry_reg_entry_time.delete(0, END)
            members_ID_time.delete(0, END)
            
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}") 
                
def search_member_timeIn_fname():
    """
    This function is for searching 
    members tru first name
    """
    strID = 'i'
    dataSearch = db['members_detail']
    search_data = dataSearch.find({
        'fname':{
            '$regex': first_name_member_reg_time.get(),
             '$options': 'i' 
            }})
   

  
    
    for j in search_data:
        member_id = j['members_id']
        l_name_search = j['lname']
        f_name_search = j['fname']
        ministry_search = j['ministry']
        
        last_name_member_reg_time.delete(0, END)
        last_name_member_reg_time.insert(0, (l_name_search))
    
        first_name_member_reg_time.delete(0, END)
        first_name_member_reg_time.insert(0, (f_name_search))
        
        ministry_reg_entry_time.delete(0, END)
        ministry_reg_entry_time.insert(0, (ministry_search))
        
        members_ID_time.delete(0, END)
        members_ID_time.insert(0, (member_id))
        
def search_member_timeIn():
    """
    This function is for searching 
    members tru ID number
    """
    dataSearch = db['members_detail']
    search_data = dataSearch.find({'members_id':{'$regex':members_ID_time.get()}})
    
    for i in search_data:
        member_id = i['members_id']
        l_name_search = i['lname']
        f_name_search = i['fname']
        ministry_search = i['ministry']
        
        last_name_member_reg_time.delete(0, END)
        last_name_member_reg_time.insert(0, (l_name_search))
    
        first_name_member_reg_time.delete(0, END)
        first_name_member_reg_time.insert(0, (f_name_search))
        
        ministry_reg_entry_time.delete(0, END)
        ministry_reg_entry_time.insert(0, (ministry_search))
        
        members_ID_time.delete(0, END)
        members_ID_time.insert(0, (member_id))

def time_in_attendace():
    """
    This function is for 
    attendance Frame
    """
    members_attendance_frame = Frame(MidViewForm9, width=950, height=400, bd=2, bg='gray', relief=SOLID)
    members_attendance_frame.place(x=20, y=8)
    
    trans_label = Label(members_attendance_frame, text='Attendance for Church Member',
                        width=35, height=1, bg='pink', fg='black',
                          font=('Arial', 15), anchor='center')
    trans_label.place(x=230, y=2)

    global dateSearch_timeIn
    dateSearch_timeIn = DateEntry(members_attendance_frame, width=15, background='darkblue',
                                  date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10)
    dateSearch_timeIn.place(x=10, y=5)
    dateSearch_timeIn.configure(justify='center')
    
    
    l_name_reg_label_time = Label(members_attendance_frame, text='ID Number:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    l_name_reg_label_time.place(x=10, y=55)

    global members_ID_time
    members_ID_time = Entry(members_attendance_frame, width=15, font=('Arial', 12))
    members_ID_time.place(x=110, y=55)

    l_name_reg_label_time = Label(members_attendance_frame, text='Last Name:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    l_name_reg_label_time.place(x=10, y=85)

    global last_name_member_reg_time
    last_name_member_reg_time = Entry(members_attendance_frame, width=15, font=('Arial', 12))
    last_name_member_reg_time.place(x=110, y=85)

    f_name_reg_label_time = Label(members_attendance_frame, text='First Name:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    f_name_reg_label_time.place(x=10, y=115)

    global first_name_member_reg_time
    first_name_member_reg_time = Entry(members_attendance_frame, width=15, font=('Arial', 12))
    first_name_member_reg_time.place(x=110, y=115)

    age_reg_label = Label(members_attendance_frame, text='Ministry:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    age_reg_label.place(x=10, y=145)

    global ministry_reg_entry_time
    ministry_reg_entry_time = ttk.Combobox(members_attendance_frame, width=20,font=('Arial', 12))
    ministry_reg_entry_time['values'] = ministry_list()
    ministry_reg_entry_time.place(x=110, y=145)

   
    btn_search = Button(members_attendance_frame, text='Search', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=7, height=1,command=search_member_timeIn)
    btn_search.place(x=250, y=55)
    
    btn_search_fname = Button(members_attendance_frame, text='Search', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=7, height=1,command=search_member_timeIn_fname)
    btn_search_fname.place(x=250, y=115)
   
    
    btn_save = Button(members_attendance_frame, text='Save', bd=2, bg='green', fg='white',
                              font=('arial', 10), width=10, height=1,command=insert_attendance)
    btn_save.place(x=10, y=185)


    memberslist_view_Form = Frame(members_attendance_frame, width=500, height=10)
    memberslist_view_Form.place(x=330, y=30)

    style = ttk.Style(members_attendance_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="cyan",
                    rowheight=15,
                    fieldbackground="yellow")
   
    
    
    global membersList_treeview
    scrollbarx = Scrollbar(memberslist_view_Form, orient=HORIZONTAL)
    scrollbary = Scrollbar(memberslist_view_Form, orient=VERTICAL)
    
    membersList_treeview = ttk.Treeview(memberslist_view_Form,
                                             columns=('Count','ID','LNAME', "FNAME","MINISTRY",
                                              'CONTACT'),
                                             selectmode="extended", height=20, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=membersList_treeview.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=membersList_treeview.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    membersList_treeview.heading('Count', text="Count", anchor=CENTER)
    membersList_treeview.heading('ID', text="ID", anchor=CENTER)
    membersList_treeview.heading('LNAME', text="Last Name", anchor=CENTER)
    membersList_treeview.heading('FNAME', text="First Name", anchor=CENTER)
    membersList_treeview.heading('MINISTRY', text="Ministry", anchor=CENTER)
    membersList_treeview.heading('CONTACT', text="Contact No.", anchor=CENTER)


    membersList_treeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    membersList_treeview.column('#1', stretch=NO, minwidth=0, width=70, anchor='e')
    membersList_treeview.column('#2', stretch=NO, minwidth=0, width=100, anchor='e')
    membersList_treeview.column('#3', stretch=NO, minwidth=0, width=100, anchor='e')
    membersList_treeview.column('#4', stretch=NO, minwidth=0, width=100, anchor='e')
    membersList_treeview.column('#5', stretch=NO, minwidth=0, width=100, anchor='e')
    membersList_treeview.column('#6', stretch=NO, minwidth=0, width=100, anchor='e')

    membersList_treeview.pack()
  
    memberList_function()
   
    
    
def memberList_function():
    
    """
    this function is for
    calling the Members List
    """
    
    membersList_treeview.delete(*membersList_treeview.get_children())
    return members_list()

def members_list():
    """
    This function is for query member's list
    """

    dataSearch = db['members_detail']
    search_data = dataSearch.find().sort('lname', pymongo.ASCENDING)

    members ={}
    count = 0
    for row in search_data:
        count+=1
        # mem_id = row['members_id']
        # Lname = row['lname']
        # fname = row['fname']
        # ministry_tr = row['ministry']
       
        
        data = {
            'members_id': row['members_id'],
            'lname': row['lname'],
            'fname': row['fname'],
            'ministry': row['ministry'],
            'contact_num': row['contact_num'],
            'count': count,
        }
        
        members.update(data)
        
        membersList_treeview.insert('', 'end', values=(members['count'],members['members_id'],members['lname'],
                                members['fname'],members['ministry'],
                                members['contact_num']))
def delete_membersDetail():
    """
    this function is for 
    deleting membersDetail
    """
    dataSearch = db['members_detail']
    query = {'members_id':{'$regex':search_input_mReg_entry.get()}}
    result = tkMessageBox.askquestion('JRS','Are you sure you want to Delete?',icon="warning")
    if result == 'yes':
        x = dataSearch.delete_one(query)
        messagebox.showinfo('JRS', 'Selected Record has been deleted')
        memberList_function()


def update_membersDetail():
    """
    this function is for updating
    members Details
    """
    dataSearch = db['members_detail']
    query = {'members_id':{'$regex':search_input_mReg_entry.get()}}

    result = tkMessageBox.askquestion('JRS','Are you sure you want to Update?',icon="warning")
    if result == 'yes':
       
        try:
            newValue = { "$set": { 
                                'lname': last_name_member_reg.get(),
                                'fname': first_name_member_reg.get(),
                                'address': add_reg_entry.get('1.0', 'end-1c'),
                                'birthday': bday_reg.get(),
                                'age': int(age_member_reg.get()),
                                'ministry': ministry_reg_entry.get(),
                                'contact_num': contact_member_reg.get()
                            }           
                        }
            dataSearch.update_many(query, newValue)
            messagebox.showinfo('JRS', 'Data has been updated')
            memberList_function()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}")

def search_member_for_update():
    """
    This function is for searching 
    member by using id number for updating 
    purposes
    """
    dataSearch = db['members_detail']
    search_data = dataSearch.find({'members_id':{'$regex':search_input_mReg_entry.get()}})
    
    for i in search_data:
        member_id = i['members_id']
        l_name_search = i['lname']
        f_name_search = i['fname']
        ministry_search = i['ministry']
        add_search = i['address']
        brithday_search = i['birthday']
        age_search = i['age']
        contactNum_search = i['contact_num']
        
        last_name_member_reg.delete(0, END)
        last_name_member_reg.insert(0, (l_name_search))
    
        first_name_member_reg.delete(0, END)
        first_name_member_reg.insert(0, (f_name_search))
        
        ministry_reg_entry.delete(0, END)
        ministry_reg_entry.insert(0, (ministry_search))
        
        add_reg_entry.delete('1.0', END) 
        add_reg_entry.insert('1.0', (add_search))

        bday_reg.delete(0, END)
        bday_reg.insert(0, (brithday_search))

        age_member_reg.delete(0, END)
        age_member_reg.insert(0, (age_search))

        contact_member_reg.delete(0, END)
        contact_member_reg.insert(0, (contactNum_search))

        search_input_mReg_entry.delete(0, END)
        search_input_mReg_entry.insert(0, (member_id))


def insert_mebers_details():
    """
    this function is for saving member
    details to mongodb
    """
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

    collection = db['members_detail']  # this part is for saving to mongodb
    dataInsert = {
        'members_id': res,
        'lname': last_name_member_reg.get(),
        'fname': first_name_member_reg.get(),
        'address': add_reg_entry.get('1.0', 'end-1c'),
        'birthday': bday_reg.get(),
        'age': int(age_member_reg.get()),
        'ministry': ministry_reg_entry.get(),
        'contact_num': contact_member_reg.get()
          
    }
    
    try:
        collection.insert_one(dataInsert)
        messagebox.showinfo('JRS', 'Data has been save')
        memberList_function()
        last_name_member_reg.delete(0, END)
        first_name_member_reg.delete(0, END)
        age_member_reg.delete(0, END)
        ministry_reg_entry.delete(0, END)
        contact_member_reg.delete(0, END)
        add_reg_entry.delete('1.0', 'end-1c')
        
    except Exception as ex:
                print("Error", f"Error due to :{str(ex)}")


def calculate_bday(e):
    """This function is to calculate age Fields """
    
    date_time_str = bday_reg.get()
   
    date_time_obj = datetime.strptime(date_time_str, '%Y-%m-%d').date()
    today = date.today()
    age = today.year - date_time_obj.year - ((today.month, today.day) < (date_time_obj.month, date_time_obj.day))

    age_member_reg.delete(0, END)
    age_member_reg.insert(0, (age))

def ministry_list():
    """
    this function is for 
    the displaying ministry to dropdown menu
    or combo box
    """  
    dataSearch = db['church_ministry'] 
    # agg_result = dataSearch.find()
    agg_result = dataSearch.find().sort('ministry', pymongo.ASCENDING)

    data = []
    for x in agg_result:
        data.append(x['ministry'])
    return data

def membersData_frame():
    """
    This is for members Data Frame
    """
    clearFrame()
    global members_data_frame
    


    members_data_frame = Frame(MidViewForm9, width=950, height=400, bd=2, bg='gray', relief=SOLID)
    members_data_frame.place(x=20, y=8)
    
    trans_label = Label(members_data_frame, text='Inserting Church Member',
                        width=35, height=1, bg='pink', fg='black',
                          font=('Arial', 13), anchor='center')
    trans_label.place(x=230, y=3)

    l_name_reg_label = Label(members_data_frame, text='Last Name:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    l_name_reg_label.place(x=10, y=30)

    global last_name_member_reg
    last_name_member_reg = Entry(members_data_frame, width=15, font=('Arial', 12))
    #userName_entry.insert(0, u'enter username')
    last_name_member_reg.place(x=110, y=30)

    f_name_reg_label = Label(members_data_frame, text='First Name:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    f_name_reg_label.place(x=10, y=55)

    global first_name_member_reg
    first_name_member_reg = Entry(members_data_frame, width=15, font=('Arial', 12))
    #userName_entry.insert(0, u'enter username')
    first_name_member_reg.place(x=110, y=55)

    add_reg_label = Label(members_data_frame, text='Address:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    add_reg_label.place(x=10, y=80)

    global add_reg_entry
    add_reg_entry = scrolledtext.ScrolledText(members_data_frame,
                                                          wrap=tk.WORD,
                                                          width=20,
                                                          height=3,
                                                          font=("Arial",
                                                                10))
    add_reg_entry.place(x=110, y=80)

   
    bdate_label = Label(members_data_frame, text='Birth Day:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    bdate_label.place(x=10, y=138)
    global bday_reg
    bday_reg = DateEntry(members_data_frame, width=15, background='darkblue', date_pattern='yyyy-MM-dd',
                                  foreground='white', borderwidth=2, padx=10, pady=10,font=('Arial', 12))
    bday_reg.place(x=110, y=138)
    bday_reg.configure(justify='center')
    bday_reg.bind("<<DateEntrySelected>>", calculate_bday)

    age_reg_label = Label(members_data_frame, text='Age:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    age_reg_label.place(x=10, y=163)

    global age_member_reg
    age_member_reg = Entry(members_data_frame, width=15, font=('Arial', 12))
    age_member_reg.place(x=110, y=163)

    age_reg_label = Label(members_data_frame, text='Ministry:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    age_reg_label.place(x=10, y=188)

    global ministry_reg_entry
    ministry_reg_entry = ttk.Combobox(members_data_frame, width=20,font=('Arial', 12))
    ministry_reg_entry['values'] = ministry_list()
    ministry_reg_entry.place(x=110, y=188)

    contact_reg_label = Label(members_data_frame, text='Contact No:', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    contact_reg_label.place(x=10, y=213)

    global contact_member_reg
    contact_member_reg = Entry(members_data_frame, width=15, font=('Arial', 12))
    contact_member_reg.place(x=110, y=213)

    search_input_mReg_label = Label(members_data_frame, text='Search ID :', width=10, height=1, bg='yellow', fg='black',
                          font=('Arial', 10), anchor='e')
    search_input_mReg_label.place(x=10, y=300)

    global search_input_mReg_entry
    search_input_mReg_entry = Entry(members_data_frame, width=15, font=('Arial', 12))
    search_input_mReg_entry.place(x=110, y=300)

    btn_search_mr = Button(members_data_frame, text='Search', bd=2, bg='yellow green', fg='black',
                              font=('arial', 10), width=10, height=1,command=search_member_for_update)
    btn_search_mr.place(x=240, y=300)
    
    
    btn_save = Button(members_data_frame, text='Save', bd=2, bg='green', fg='white',
                              font=('arial', 10), width=10, height=1,command=insert_mebers_details)
    btn_save.place(x=10, y=243)

    btn_update = Button(members_data_frame, text='Update', bd=2, bg='blue', fg='white',
                              font=('arial', 10), width=10, height=1,command=update_membersDetail)
    btn_update.place(x=110, y=243)

    btn_delete = Button(members_data_frame, text='Delete', bd=2, bg='red', fg='white',
                              font=('arial', 10), width=10, height=1,command=delete_membersDetail)
    btn_delete.place(x=210, y=243)


    memberslist_view_Form = Frame(members_data_frame, width=500, height=10)
    memberslist_view_Form.place(x=330, y=30)

    style = ttk.Style(members_data_frame)
    style.theme_use("clam")
    style.configure("Treeview",
                    background="black",
                    foreground="white",
                    rowheight=15,
                    fieldbackground="yellow")
   
    
    
    global membersList_treeview
    scrollbarx = Scrollbar(memberslist_view_Form, orient=HORIZONTAL)
    scrollbary = Scrollbar(memberslist_view_Form, orient=VERTICAL)
    
    membersList_treeview = ttk.Treeview(memberslist_view_Form,
                                             columns=('Count','ID','LNAME', "FNAME","MINISTRY",
                                              'CONTACT'),
                                             selectmode="extended", height=20, yscrollcommand=scrollbary.set,
                                             xscrollcommand=scrollbarx.set)
    scrollbary.config(command=membersList_treeview.yview)
    scrollbary.pack(side=RIGHT, fill=Y)
    scrollbarx.config(command=membersList_treeview.xview)
    scrollbarx.pack(side=BOTTOM, fill=X)
    membersList_treeview.heading('Count', text="Count", anchor=CENTER)
    membersList_treeview.heading('ID', text="ID", anchor=CENTER)
    membersList_treeview.heading('LNAME', text="Last Name", anchor=CENTER)
    membersList_treeview.heading('FNAME', text="First Name", anchor=CENTER)
    membersList_treeview.heading('MINISTRY', text="Ministry", anchor=CENTER)
    membersList_treeview.heading('CONTACT', text="Contact No.", anchor=CENTER)


    membersList_treeview.column('#0', stretch=NO, minwidth=0, width=0, anchor='e')
    membersList_treeview.column('#1', stretch=NO, minwidth=0, width=70, anchor='e')
    membersList_treeview.column('#2', stretch=NO, minwidth=0, width=100, anchor='e')
    membersList_treeview.column('#3', stretch=NO, minwidth=0, width=100, anchor='e')
    membersList_treeview.column('#4', stretch=NO, minwidth=0, width=100, anchor='e')
    membersList_treeview.column('#5', stretch=NO, minwidth=0, width=100, anchor='e')
    membersList_treeview.column('#6', stretch=NO, minwidth=0, width=100, anchor='e')

    membersList_treeview.pack()
  
    memberList_function()

#===========================================User Registration Frame====================================
def insert_user_registration():
    """
    This function is for inserting
    user registration
    """

    
    if userName_entry_registry.get == "" or password_entry_registration.get() == "":
            lbl_result_registration.config(text="Please complete the required field!", fg="red")
    elif password_entry_registration.get() != password_register_Reentry.get():
            lbl_result_registration.config(text="Password did not Match", fg="red")
    else:
        

        collection = db['admin_login']

        dataInsert = {
            'fullname': full_name_registry.get(),
            'username': userName_entry_registry.get(),
            'password': password_entry_registration.get(),
            'status': 'for approval',
            'created':datetime.now()
            
        }
        
        try:
            collection.insert_one(dataInsert)
            messagebox.showinfo('JRS','Data has been saved')
            registration_frame.destroy()
        except Exception as ex:
            messagebox.showerror("Error", f"Error due to :{str(ex)}")
            
    
# =====================================Registration =============================================
def user_regsitration_frame():
    """
    This function is for
    user registration 
    """
    global registration_frame
    registration_frame = Toplevel()
    registration_frame.title("User Regsitration")
    width = 550
    height = 400
    screen_width = registration_frame.winfo_screenwidth()
    screen_height = registration_frame.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    registration_frame.geometry("%dx%d+%d+%d" % (width, height, x, y))
    registration_frame.resizable = True
    registration_frame.config(bg="cyan")



    full_name_label = Label(registration_frame,text='Full Name',width=14,height=1,bg='yellow',fg='black',
                                font=('Arial',11),anchor='c')
    full_name_label.place(x=100,y=130)

    global full_name_registry
    full_name_registry = Entry(registration_frame, width=22, font=('Arial', 12))
    #userName_entry.insert(0, u'enter username')
    full_name_registry.place(x=250, y=130)

    username_lbl = Label(registration_frame,text='Username',width=14,height=1,bg='yellow',fg='black',
                                font=('Arial',11),anchor='c')
    username_lbl.place(x=100,y=160)

    global userName_entry_registry
    userName_entry_registry = Entry(registration_frame, width=22, font=('Arial', 12))
    #userName_entry.insert(0, u'enter username')
    userName_entry_registry.place(x=250, y=160)


    password_lbl = Label(registration_frame,text='Password',width=14,height=1,bg='yellow',fg='black',
                                font=('Arial',11),anchor='c')
    password_lbl.place(x=100,y=190)

    global password_entry_registration
    password_entry_registration = Entry(registration_frame, width=22, font=('Arial', 12),show="*")
    #password_entry.insert(0,u'enter password')
    password_entry_registration.place(x=250, y=190)


    password_lbl_retype = Label(registration_frame,text='Password Retype',width=14,height=1,bg='yellow',fg='black',
                                font=('Arial',11),anchor='c')
    password_lbl_retype.place(x=100,y=220)

    global password_register_Reentry
    password_register_Reentry = Entry(registration_frame, width=22, font=('Arial', 12),show="*")
    #password_entry.insert(0,u'enter password')
    password_register_Reentry.place(x=250, y=220)

    global lbl_result_registration
    lbl_result_registration = Label(registration_frame, text="", bg='skyblue', font=('arial', 13),anchor='c')
    lbl_result_registration.place(x=100, y=250)


    btn_login = Button(registration_frame, text="Register", font=('arial', 12), width=39,
                        command= insert_user_registration)
    btn_login.place(x=100, y=270)
    # btn_login.bind('<Return>', Login),
#=================================================log out Frame =======================================
def Logout():
    result = tkMessageBox.askquestion('JRS System', 'Are you sure you want to logout?', icon="warning")
    if result == 'yes':

        root.deiconify()
        reportFrame.destroy()
#=================================================dashboard Frame =======================================
def dashboard():
    
    
    global MidViewForm9
    global logo_icon2
    global reportFrame

    reportFrame = Toplevel()
    reportFrame.title("DashBoard")
    width = 1000
    height = 500
    screen_width = reportFrame.winfo_screenwidth()
    screen_height = reportFrame.winfo_screenheight()
    x = (screen_width / 2) - (width / 2)
    y = (screen_height / 2) - (height / 2)
    reportFrame.geometry("%dx%d+%d+%d" % (width, height, x, y))
    reportFrame.resizable = True

#=============================================Frame for time & others in DashBoard======================================
    TopdashboardForm = Frame(reportFrame, width=1295, height=50, bd=2, relief=SOLID)
    TopdashboardForm.place(x=1,y=8)
#============================================================= menu Bar=================================================
    
    global filemenu2
    menubar = Menu(reportFrame)
    filemenu = Menu(menubar, tearoff=0)
    filemenu2 = Menu(menubar, tearoff=0)
    filemenu3 = Menu(menubar, tearoff=0)
    filemenu4 = Menu(menubar, tearoff=0)
    filemenu5 = Menu(menubar, tearoff=0)
    filemenu6 = Menu(menubar, tearoff=0)
    filemenu7 = Menu(menubar, tearoff=0)

    filemenu.add_command(label="Logout", command = Logout)
    # filemenu.add_command(label="Exit")
    # filemenu2.add_command(label="User Approval",command=user_approvalFrame)
    # filemenu2.add_command(label="Checker & Approver",command=check_by_frame)

   
    time_in_attendace
    filemenu3.add_command(label="Member Registration",command=membersData_frame)
    filemenu3.add_command(label="Time In",command=time_in_attendace)
    
    # for report frame menu
    
    filemenu5.add_command(label="Data per Ministry",command=report_piechart_members_Data)
    filemenu5.add_command(label="Graph per Date Service",command=graph_attendance)
    filemenu5.add_command(label="Attendance Chart",command=members_attendanceComposition_frame)
    filemenu5.add_command(label="BirthDay of The Month",command=birthday_list_frame)
    filemenu5.add_command(label="Attendance per Sunday",command=attendance_list_frame)
    filemenu5.add_command(label="Absent per Sunday",command=absent_members_frame)

    filemenu7.add_command(label="Back up Data",command=backuData)  


    # this is for accounting frame
    filemenu4.add_command(label="Insert Chart of Account",command=chart_of_account)
    filemenu4.add_command(label="Journal Entry",command=journal_entry)
    
    menubar.add_cascade(label="Account", menu=filemenu)
    menubar.add_cascade(label="User Approval", menu=filemenu2)
    menubar.add_cascade(label="Attendance", menu=filemenu3)
    menubar.add_cascade(label="Accounting Transaction", menu=filemenu4)
    
    menubar.add_cascade(label="Inventory", menu=filemenu6)
    menubar.add_cascade(label="Reports", menu=filemenu5)
    menubar.add_cascade(label="Back up", menu=filemenu7)

    reportFrame.config(menu=menubar)

    
      
        # filemenu2["state"] = DISABLED

    # disable_userApproval()
    MidViewForm9 = Frame(reportFrame, width=1295, height=600,bd=2,relief=SOLID)
    MidViewForm9.place(x=1, y=58)
    MidViewForm9.config(bg="cyan")


    # load2 = PIL.Image.open("image\search2.jpg")
    # load2 = load2.resize((125, 50), PIL.Image.ANTIALIAS)
    # logo_icon2 = ImageTk.PhotoImage(load2)

    UserName = userName_entry.get()
    user_label = Label(TopdashboardForm, text='Sign in as', width=17, height=1, bg='yellow', fg='gray',
                      font=('Arial', 11), anchor='c')
    user_label.place(x=5, y=15)


    user_Name_label = Label(TopdashboardForm, text='', width=17, height=1, bg='yellow', fg='gray',
                       font=('Arial', 11), anchor='c')
    user_Name_label.place(x=175, y=15)
    user_Name_label.config(text=UserName, fg="red")

    # :%a, %b %d %Y
    DateTime_label = Label(TopdashboardForm, text=f"{dt.datetime.now():%a, %b %d %Y %I:%M %p}",
                           fg="white", bg="black", font=("helvetica", 10))
    DateTime_label.place(x=700, y=15)


#=================================================log in Function ========================================
def Login():
    
    if USERNAME.get == "" or PASSWORD.get() == "":
            lbl_result.config(text="Please complete the required field!", fg="red")
    else:
        dataSearch = db['admin_login']

        # query = dataSearch.find_one({'name': USERNAME.get(), 'password':PASSWORD.get()})
        query = {'username': USERNAME.get(), 'password':PASSWORD.get(),'status':'approved'}
        agg_result = dataSearch.count_documents(query)

        
        if agg_result > 0:

            PASSWORD.set("")
            lbl_result.config(text="")
            root.withdraw()
            dashboard()

        else:

            lbl_result.config(text="Invalid Username or Password", fg="red")
            USERNAME.set("")
            PASSWORD.set("")

           

                

       



#=============================================STring Bar for Log in ======================================
USERNAME =StringVar()
PASSWORD = StringVar()

# ================================================= LOG IN FRAME===========================================


global userName_entry
global password_entry
logolbl = Label(root,image= logo_icon)
logolbl.place(x=300,y=120)

welcome_label =  Label(root,text='WELCOME TO ARISE CHURCH SYSTEM',width=35,height=2,bg='yellow',fg='black',
                            font=('Arial',20),anchor='c')
welcome_label.place(x=100,y=30)

# loginlabe = Label(root,text='Sign in as',width=17,height=1,bg='yellow',fg='',
#                             font=('Arial',14),anchor='c')
# loginlabe.place(x=350,y=100)

# user_description = ttk.Combobox(root, width=19,font=('Arial',13))
# user_description['values'] = ("Admin", "Employee")
# user_description.place(x=350, y=105)

username_lbl = Label(root,text='Username',width=14,height=1,bg='yellow',fg='black',
                            font=('Arial',11),anchor='c')
username_lbl.place(x=200,y=260)

userName_entry = Entry(root, width=22,textvariable = USERNAME, font=('Arial', 12))
#userName_entry.insert(0, u'enter username')
userName_entry.place(x=350, y=260)


password_lbl = Label(root,text='Password',width=14,height=1,bg='yellow',fg='black',
                            font=('Arial',11),anchor='c')
password_lbl.place(x=200,y=290)

password_entry = Entry(root, width=22,textvariable = PASSWORD, font=('Arial', 12),show="*")
#password_entry.insert(0,u'enter password')
password_entry.place(x=350, y=290)

lbl_result = Label(root, text="", bg='cyan', font=('arial', 13),anchor='c')
lbl_result.place(x=200, y=320)


btn_login = Button(root, text="Login", font=('arial', 12), width=39,command=Login)
btn_login.place(x=200, y=340)
# btn_login.bind('<Return>', Login),

password_lbl = Label(root,text='If not Register, click button?',width=25,height=1,
                            font=('Arial',10),anchor='c')
password_lbl.place(x=170,y=390)

btn_registration = Button(root, text="Registration", font=('arial', 12),
                                 width=17,bg='gray',fg='yellow', command=user_regsitration_frame
                                )
btn_registration.place(x=380, y=390)

# ========================================INITIALIZATION===================================
if __name__ == '__main__':
    root.mainloop()


