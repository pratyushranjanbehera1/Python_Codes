#WAP to display the list of records from table employee
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="test")
mycursor=mydb.cursor()
mycursor.execute("select * from employee")
for data in mycursor:
    print(data)
mydb.close()
