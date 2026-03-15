import mysql.connector

mycon=mysql.connector.connect(host="localhost",user='root', passwd='tiger',database='test')

if mycon.is_connected()==False:
    print("Unable to connect")
    
cursor=mycon.cursor()
cursor.execute("""insert into customer(ccode,cname,balance)
    values(1006,'Abhishek Hota',4500)""")

mycon.commit()
cursor.execute('''select * from customer''')
for x in cursor:
    print (x)

mycon.close()
