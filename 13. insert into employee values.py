import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='tiger',database='test')
cursor=mydb.cursor()
cursor.execute('''insert into employee values(105,"Aditya","Manager",90000,"2018-05-07")''')
mydb.commit()
mydb.close()
