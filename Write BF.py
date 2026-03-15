#WAP to add/insert records in to a binary file student.dat
import pickle
file=open("student.dat",'wb')
while True:
    rno=int(input("Enter roll no.:"))
    name=input("Enter name:")
    marks=float(input("Enter Percentage of marks:"))
    rec=[rno,name,marks]
    pickle.dump(rec,file)
    choice=input("Do you want to add more records:(y/n):")
    if choice=='n':
        break
file.close()
            
