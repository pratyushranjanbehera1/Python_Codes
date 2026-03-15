import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",passwd="tiger"
,database="test")
mycursor=mydb.cursor()
mycursor.execute("delete from student where no=3")
mydb.commit()

mydb.close()
