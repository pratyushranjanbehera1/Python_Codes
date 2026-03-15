#WAP to calculate the Displacement using function.
def DispCalc(u,t,a):
    s=u*t+0.5*a*t**2
    return s
X=int(input("Enter the Initial Velocity: "))
Y=int(input("Enter the Time: "))
Z=int(input("Enter the Acceleration: "))
calc=DispCalc(X,Y,Z)
print("Calculated Displacement is: ",calc)
