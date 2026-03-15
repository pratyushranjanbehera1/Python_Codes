#WAP to read records from a binary file student.dat display the list of students .
import pickle
file=open("student.dat",'rb')
print("The list of students is:")
rec=pickle.load(file)
for r in rec:
    print(r)
file.close()


