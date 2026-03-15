import mysql.connector
mydb=mysql.connector.connect(host='localhost',user='root',password='tiger',database='test')
cursor=mydb.cursor()
ch=1
while ch==1:
    ecode=int(input("Enter employee code:"))
    ename=input("Enter name:")
    edesig=input("Enter designation:")
    esalary=float(input("Enter salary:"))
    doj=input("Enter date of joining:")
    cursor.execute("insert into employee values('''+str(ecode)+''','''+ename+''','''+edesig+''','''+str(esalary)+''','''+doj+''')")
    mydb.commit()
    ch=input("Do you want to add more records:1-yes 0-No:")
mydb.close()
