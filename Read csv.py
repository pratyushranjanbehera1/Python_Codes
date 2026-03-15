# WAP to read the contents of a csv file student.csv
import csv
file=open("student.csv","r",newline='')
records = csv.reader(file)
for row in records:
    print(row)

file.close()

