# WAP to fetch all records using fetchone() from a table at run time
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="test")
mycursor=mydb.cursor()
mycursor.execute("select * from employee")
myrecords=mycursor.fetchone()
while myrecords is not None:
    print(myrecords)
    myrecords=mycursor.fetchone()

mydb.close()
