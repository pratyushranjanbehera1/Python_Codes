import mysql.connector
mydb=mysql.connector.connect(host='localhost',database='test',user='root',password='tiger')
mc=mydb.cursor()
mc.execute("Show tables")
print(mc)
for i in mc:
    print(i)
