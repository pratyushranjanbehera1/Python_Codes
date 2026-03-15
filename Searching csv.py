#WAP to search the record of a particular student from the file student.csv
# on the basis of given roll no.
import csv
file=open('student.csv',"r", newline='')
records = csv.reader(file)
found=0
rno=input("Enter the roll no to be searched:")
for row in records:
    if row[0]==rno:
        print("The search record is:",row)
        found=1
        break
if found==0:
    print("Record not found")

file.close()







