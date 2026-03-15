#WAP to read records from a binary file student.dat display the list of students .
import pickle
file=open("student.dat",'rb')
print("The list of students is:")
try:
    while True:
        rec=pickle.load(file)
        rno=rec[0]
        name=rec[1]
        marks=rec[2]
        print(rno,name,marks)
except EOFError:
    file.close()


