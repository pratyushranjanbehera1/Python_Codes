#WAP to calculate the KE PE and E total energy
m=int(input("Enter the Mass: "))
v=int(input("Enter the  velocity: "))
g=float(input("Enter the gravity: "))
h=int(input("Enter the height: "))
KE=0.5*m*v**2
PE=m*g*h
E=KE+PE
print("Calculated Kenitic Energy: ",KE)
print("Calculated Potential Energy: ",PE)
print("Calculated total Energy: ",E)            
