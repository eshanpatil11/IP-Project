import numpy as np
import pandas as pd
import mysql.connector as con
import matplotlib.pyplot as mp

c = con.connect(host="localhost",user="root",passwd="Dhruv@2025",database='ip_project')
cursor=c.cursor()

df1=pd.read_sql("SELECT * FROM ip_project.auth_table;", c)
#print(df1)

def class_report(s):
    #dfverify = pd.read_sql("SELECT * FROM votingsys.admin_credentials WHERE uid='{}' and password='{}';".format(uid,password), mycon)
    df2 = pd.read_sql("SELECT * FROM ip_project.student_info where Class_ID = '{}';".format(s), c)
    #print(df2)
    l1 = []
    names=[]
    for (row,rowseries) in df2.iterrows():
        t = rowseries["Math"]+rowseries["Science"]+rowseries["English"]+rowseries["SST"]+rowseries["Hindi"]+rowseries["AI/MM"]
        l1.append(t)
        names.append(rowseries['Name'])
#        print(row,rowseries)
    df2["Total"] = l1
    print(l1)
    #print(df2)  
    l=[]
    mp.pie(df2["Total"],labels=names )
    mp.legend()
    mp.title("Marks Distribution of students")
    mp.show()
    '''
    x = df2["Math"]
    print(x)
    lb = df2["Name"]
    mp.title(s)
    mp.pie(x, labels = lb, autopct = "%5.1f%%")
    mp.legend()
    mp.show()  '''

def student_report(s):
    stuid=int(input("Enter student id" ))
    df3 = pd.read_sql("SELECT * FROM ip_project.student_info where Class_ID = '{}'and Student_ID='{}';".format(s,stuid), c)
    print(df3)
    marks=0
    sub=['Math','Science','English','SST','Hindi','AI/MM']
    ma=[]
    #a=np.empty(3)
    for (cols,coitem) in df3.items():
        print(cols,"has ",coitem.values)
        
        if cols=='Math'or cols=='Science' or cols=='English':
            #marks+=coitem
            ma.append(coitem.values)
        a=np.array(ma)
        print(a)
        mp.bar(ma,sub)
        mp.show()
            
    print(a)   
    '''m=cols['Math']
        sc=cols['Science']
        marks.append(coitem['English'])
        marks.append(coitem['SST'])
        marks.append(coitem['Hindi'])
        marks.append(coitem['AI/MM'])'''
    #print(m,sc)


    
def welcome(s):
    print("Welcome Teacher, Whats on your mind?",s)
    ch = int(input("Classwise = 1, Studentwise = 2: "))
    if ch == 1:
        class_report(s)
        print("Classwise Report")
    elif ch == 2:
        print("Studentwise Report")
        student_report(s)
    else:
        print("Wrong Choice")    

def auth_user():
    uid = input("Enter User ID: ")
    passwd = input("Enter Password: ")
    for (row,rowseries) in df1.iterrows():
        #print(row,rowseries)
        #print(rowseries["User_ID"],uid,"hey", rowseries["Pass"],passwd)
        if uid== rowseries["User_ID"] and passwd == rowseries["Pass"]:
            print("Valid user")
            cID=rowseries['Class_ID']
            welcome(cID)

auth_user()


