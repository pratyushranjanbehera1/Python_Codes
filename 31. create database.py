#WAP to Create a database
import mysql.connector 
mydb=mysql.connector.connect(host="localhost",user='root', password='ruby@sql',)
mycursor=mydb.cursor()
mycursor.execute('create database puspadatabase')
print("Table created successfully!!!!")
#Closing the connection
mydb.close()
