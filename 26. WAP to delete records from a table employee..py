# WAP to delete records from a table employee.

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="test") 
mycursor=mydb.cursor()
mycursor.execute("delete from employee where ecode=101")
mydb.commit()

print("Record deleted....")
mydb.close()
