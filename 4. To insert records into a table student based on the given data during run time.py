#To insert records into a table student based on the given data during run time
import mysql.connector
mydb=mysql.connector.connect(host="localhost", user="root",password="ruby@sql",database="test")
print(mydb)
mycursor=mydb.cursor()
while True:
    L=[]
    roll=int(input("Enter the roll number : "))
    L.append(roll)
    name=input("Enter the Name: ")
    L.append(name)
    age=int(input("Enter Age of Student : "))
    L.append(age)
    clas=input("Enter the Class : ")
    L.append(clas)
    city=input("Enter the City of the Student : ")
    L.append(city)
    sql="insert into student2 (roll,name,age,class,city) values (%s,%s,%s,%s,%s)"
    mycursor.execute(sql,L)
    mydb.commit()
    choice=input("Do you want to add more records:y/n:")
    if choice=='n':
        break
mydb.close()
