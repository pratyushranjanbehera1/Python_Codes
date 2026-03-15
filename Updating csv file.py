# WAP to modify data in a CSV file "student.csv".
import csv
file=open("student.csv","r",newline='')
records = csv.reader(file)
rno=input("Enter the roll no to be modified:")
rec=[]
for row in records:
    if row[0]==rno:
        print("Existing name is :",row[1])
        name=input("Enter new name:")
        row[1]=name
    rec.append(row)
file.close()

file=open("student.csv","w",newline='')
writer=csv.writer(file)
writer.writerows(rec)
file.close()
