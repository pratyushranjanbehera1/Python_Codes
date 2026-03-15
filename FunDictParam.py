#WAP to calculate the sum and average marks of a student
#by passing ditionary as an argument
def Calculate(MDict):
    sum=avg=0
    for i in MDict:
        sum=sum+MDict[i]
    avg=sum/3
    return (sum,avg)
name=eval(input("Enter name within quotes:"))
MyDict={"Eng":65,"Math":82,"Science":75}
sm,av=Calculate(MyDict)
print("Name of the student: ",name)
print("Total marks: ",sm)
print("Average marks: ",av)
