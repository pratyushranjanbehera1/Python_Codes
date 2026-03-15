import mysql.connector
mycon= mysql.connector.connect(host="localhost",user="root", password="tiger", database="test")
cursor= mycon.cursor()
cursor.execute("drop table if exists teacher")

cursor.execute("create table teacher (Tcode int(4), Tname char(30), Tsalary float(8,2), Dept char(30))")

mycon.close()
