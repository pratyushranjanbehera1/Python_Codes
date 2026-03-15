import pickle
F=open("student.dat", "rb+")
roll=int(input("Enter Roll no of the student to be updated "))
found=0
try:
    while True:
        pos=F.tell()
        R=pickle.load(F)
        if R[0]==roll:
            print("Existing percentage of marks is:",R[2])
            R[2]=float(input("Enter new percentage of marks "))
            F.seek(pos)
            pickle.dump(R,F)
            found+=1
except EOFError:
    if found==0:
        print("Record not found !!!!")
    else:
        print("Record updated successfully.......") 
    F.close()
