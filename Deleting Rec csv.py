#WAP to delete records from a csv file student.csv

import csv                                            
record= []
name=input("Enter a student name which you want to delete:")
with open("student.csv" , "r",newline='') as file:
    data= csv.reader(file)                          
    for row in data:
        record.append(row)
        for field in row:
            if field==name:
                record.pop()
file.close()
myfile=open("student.csv","w",newline='')
writer_obj= csv.writer(myfile)                       
writer_obj.writerows(record)           
myfile.close()                                        

