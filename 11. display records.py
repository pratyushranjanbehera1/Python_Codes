import mysql.connector

mycon=mysql.connector.connect(host="localhost",user='root', passwd='tiger',database='test')

if mycon.is_connected()==False:
    print("Unable to connect")
    
cursor=mycon.cursor()
cursor.execute("insert into teacher(Tcode,Tname,Tsalary,Dept) values(1006,'Abhishek Hota',52000,'computer science')")

mycon.commit()
#display records
cursor.execute('''select * from teacher''')
for x in cursor:
    print (x)

mycon.close()
