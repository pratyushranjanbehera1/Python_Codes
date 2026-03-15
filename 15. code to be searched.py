#To search records from a table
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="test")
mycursor=mydb.cursor()
ecod=input("Enter employee code to be searched:")
e1=(ecod,)
sql="select * from employee where ecode=%s"
mycursor.execute(sql,e1)
for x in mycursor:
    print(x)
mydb.close()
