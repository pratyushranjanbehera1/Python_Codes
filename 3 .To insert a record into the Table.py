#To insert a record into the Table
import mysql.connector

mycon=mysql.connector.connect(host="localhost",user='root', password='tiger',database='test')

if mycon.is_connected()==False:
    print("Unable to connect")
    
cursor=mycon.cursor()
sql="""insert into employee3
values(1005,'Anil Kumar','Manager',8500)"""
cursor.execute(sql)
mycon.commit()
mycon.close()
