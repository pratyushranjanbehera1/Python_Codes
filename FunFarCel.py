#WAP to Convert Celsius to Fahrenheit using function and vice versa
def Fahre_celc(celsius):
    f=(celsius*1.8)+32
    return f
def Celc_Fahre(Fahrenheit):
    c=(Fahrenheit-32)/1.8
    return c
print("Enter your choice \n1.Fahrenheit \n2.Celsius")
ch=int(input("Enter your choice: "))
if ch==1:
    c=float(input("Enter temperature celsius: "))
    f=Fahre_celc(c)
    print("After convertaion the Fahrenheit temperature is: ",f)
else:
    f=float(input("Enter temperature Fahrenheit: "))
    c=Celc_Fahre(f)
    print("After convertaion the celsius temperature is: ",c)



