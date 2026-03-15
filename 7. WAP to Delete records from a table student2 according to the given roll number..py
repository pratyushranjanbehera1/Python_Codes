#WAP to Delete records from a table student2 according to the given roll number.
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger",database="test")
print(mydb)
mycursor=mydb.cursor()
rno=int(input("Enter roll no to be deleted : "))
r1=(rno,)
sql="Delete from student2 where roll=%s"
mycursor.execute(sql,r1)
print('Record deleted!!!')
mydb.commit()
mydb.close()
    

