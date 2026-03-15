#WAP to calculate the si using function.
def SiCalc(p,r,t):
    si=p*r*t/100
    return si
X=int(input("Enter the Principal amount: "))
Y=float(input("Enter the Rate of Intrest: "))
Z=int(input("Enter the Time period: "))
calc=SiCalc(X,Y,Z)
print("Calculated simple intrest is: ",calc)
