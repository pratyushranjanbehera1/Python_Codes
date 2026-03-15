# WAP to fetch all records of a table at run time using fetchall()
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="test")
mycursor=mydb.cursor()
mycursor.execute("select * from student2")
row=mycursor.fetchall()
for data in row:
    print(data)
mydb.close()

