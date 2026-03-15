#To check the successful connectivity with Python.
import mysql.connector
mydb = mysql.connector.connect(host="localhost",user="root",password="ruby@sql")
if mydb.is_connected():
	print("Successful")


