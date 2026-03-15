#WAP to read records from a binary file student.dat display the list of
#students whose mark is above 95.0.
import pickle
file=open("student.dat",'rb')
print("The list of students whose Percentage of mark is above 90% ....")
try:
    while True:
        rec=pickle.load(file)
        if rec[2]>=90:
            print(rec)
except EOFError:
    file.close()
