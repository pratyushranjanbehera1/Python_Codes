import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='tiger',database='test')
cursor=mydb.cursor()
cursor.execute("drop table if exists employee")
sql="create table employee (ecode int(3),ename char(20),edesig char(20),esalary float(8,2),doj date)"
cursor.execute(sql)
mydb.close()
