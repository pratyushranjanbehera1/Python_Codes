# WAP to fetch all records of a table at run time
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="test")
mycursor=mydb.cursor()
mycursor.execute("select * from student")
myrecords=mycursor.fetchall()
for x in myrecords:
    print (x)
mydb.close()
