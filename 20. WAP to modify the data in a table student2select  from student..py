# WAP to modify the data in a table student2select * from student.
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="test")
mycursor=mydb.cursor()
mycursor.execute("update student2 set age=19 where roll=3")
print("Record updated !!!!")
mydb.commit()
mydb.close()
