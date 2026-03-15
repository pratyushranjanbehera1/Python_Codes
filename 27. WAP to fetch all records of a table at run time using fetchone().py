# WAP to fetch all records of a table at run time using fetchone()
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="test")
mycursor=mydb.cursor()
mycursor.execute("select * from student2")

row=mycursor.fetchone()
while row is not None:
    print(row)
    row = mycursor.fetchone()
mydb.close()
