# WAP to search & display specific records from table employee according to the given condition

import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="test")
mycursor=mydb.cursor()

mycursor.execute("select * from employee where edesig='PGT'")
for data in mycursor:
    print(data)
mydb.close()

