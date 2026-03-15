# To insert records into the table student
import os
import platform
import mysql.connector

mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="tiger",
                             database="test")
print(mydb)
mycursor=mydb.cursor()
L=[]
no=int(input("Enter the roll number : "))
L.append(no)
name=input("Enter the Name: ")
L.append(name)
age=int(input("Enter Age of Student : "))
L.append(age)
department=input("Enter the department of the Student : ")
L.append(department)
fee=float(input("Enter the fee : "))
L.append(fee)
sex=input("Enter the sex of the Student : ")
L.append(sex)
stud=(L)
sql="insert into student (no,name,age,department,fee,sex) values (%s,%s,%s,%s,%s,%s)"
mycursor.execute(sql,stud)
mydb.commit()
mydb.close()
