#WAP to read, count and display the list of all the  records present in a table student using fetchall().
import mysql.connector
mydb=mysql.connector.connect(host="localhost",user="root",password="tiger",database="test")
mycursor=mydb.cursor()

mycursor.execute("select * from student")
rec=mycursor.fetchall()
count=mycursor.rowcount
print("The total number of records in table student is:", count)

for data in rec:
    print(data)
mydb.close()


'''fetchall() : This function is used to fetch all the rows/ records from the resultset
in the form of a tuple containing records.

rowcount : This command is used to count the number of records returned by SQL query.'''
