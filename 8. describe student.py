import mysql.connector
mycon= mysql.connector.connect(host="localhost",user="root", password="tiger", database="test")
cur= mycon.cursor()
#cur.execute('''create table customer (ccode int(4), cname char(30), balance float(6,2))''')
cur.execute('''describe student2''')
for x in cur:
    print(cur)
mycon.close()
