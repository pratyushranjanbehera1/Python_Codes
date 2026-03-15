# WAP to fetch specified number of records from a table "student2" using fetchmany().
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="test")
mycursor=mydb.cursor()
mycursor.execute("select * from student2")
myrecords=mycursor.fetchmany(2)
for data in myrecords:
    print(data)


mydb.close()



