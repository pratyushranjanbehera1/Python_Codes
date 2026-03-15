#WAP to calcalculate the sum of two number using function
def sum(a,b):
    add=a+b
    return add
for i in range(1,4):
    x=int(input("Enter the first number:- "))
    y=int(input("Enter the second number:- "))
    res=sum(x,y)
    print("Sum of the numbers is",res)
