# WAP to fetch one record of a table at run time
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="test")
mycursor=mydb.cursor()
mycursor.execute("select * from student")
row1=mycursor.fetchone()
row2=mycursor.fetchone()

print(row1)
print(row2)

mydb.close()
