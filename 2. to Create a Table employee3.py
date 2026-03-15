#WAP to Create a Table employee3
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user='root', password='ruby@sql',database='omm')
if mydb.is_connected()==False:
    print("Unable to connect")
mycursor=mydb.cursor()
sql ='''CREATE TABLE EMPLOYEE(
ECODE INT(4),
NAME CHAR(30),
DESIG CHAR(20),
SALARY FLOAT(6,2))'''
mycursor.execute(sql)
print("Table created successfully!!!!")
#Closing the connection
mydb.close()
