#WAP to delete a record from table student according to the given roll no
import mysql.connector

mydb=mysql.connector.connect(host="localhost",
                             user="root",
                             password="tiger",
                             database="test")
print(mydb)
mycursor=mydb.cursor()

no=int(input("Enter roll of to be deleted : "))
roll=(no,)
sql="Delete from STUDENT where no=%s"
mycursor.execute(sql,roll)

print('Record deleted!!!')
mydb.commit()
mydb.close()
