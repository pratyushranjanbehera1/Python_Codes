import mysql.connector

mycon=mysql.connector.connect(host="localhost",user='root', passwd='tiger',database='test')

if mycon.is_connected()==False:
    print("Unable to connect")
    
cursor=mycon.cursor()

while(1):
    
    print("---------------------------")
    print("1.Add record into table")
    print("2.display record from table")
    print("3.exit program")
    print("---------------------------")
    c=int(input(" Enter your choice (1/2/3):"))
    if c==1:
        t=input('your query to add/update record-> ')
        cursor.execute(t)
        mycon.commit()

    elif c==2:
        t=input('your query to show record-> ')
        cursor.execute(t)
        d=cursor.fetchall()
        print(cursor.column_names)
        for r in d:
            print(r)
    elif c==3:
        break

mycon.close()
    
'''
while(True):
    data=cursor.fetchone()
    if(data==None):
        break
    print(data)
'''   


