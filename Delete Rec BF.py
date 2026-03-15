#WAP to delete records from a binary file student.dat based on given roll no.
import pickle
file=open("student.dat",'rb')
roll=int(input("Enter the roll number to be deleted"))
records=[]
try:
    while True:
        rec=pickle.load(file)
        if rec[0]==roll:
            continue
        records.append(rec)
except EOFError:
    file.close()
    
file=open("student.dat",'wb')
pickle.dump(records,file)
file.close()
