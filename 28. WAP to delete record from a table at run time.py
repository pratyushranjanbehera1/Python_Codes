# WAP to delete record from a table at run time
import mysql.connector

mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             passwd="tiger",
                             database="test")
print(mydb)
mycursor=mydb.cursor()

ecode=int(input("Enter employee code to be deleted : "))
rl=(ecode,)

sql="delete from employee where ecode=%s"
mycursor.execute(sql,rl)
print('Record deleted!!!')
mydb.commit()
