#WAP to accept any 3 number and find the largest among them
#using if else statement.
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
c=int(input("Enter the third number: "))
if a>b:
    if a>c:
        print(a,"is larger than",b," and ",c)
    else:
        print(c,"is larger than",a," and ",b)
else:
    if b>c:
        print(b,"is larger than",a," and ",c)
    else:
        print(c,"is larger than",a," and ",b)  
        
