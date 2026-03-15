# WAP to write data into a CSV file "student3.csv".
import csv
file=open("student.csv","w",newline='')
fields=['rno','name','total']
writer=csv.writer(file)
writer.writerow(fields)
while True:
    rn=int(input("Enter roll number:"))
    name=input("Enter name:")
    tot=float(input("Enter total marks:"))
    data=[rn,name,tot]
    writer.writerow(data)
    choice=input("Do you want to add more records:y/n:")
    if choice=='n':
        break
file.close()



    
