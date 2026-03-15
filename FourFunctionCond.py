'''WAP to create a five function calculator by choosing the
arithematic operator'''
Result=0
val1=float(input("Enter value 1:"))
val2=float(input("Enter value 2:"))
op=input("Enter any of the operator(+,-,*,/,%): ")
if op=='+':
    Result=val1+val2
elif op=='-':
    if val1>val2:
        Result=val1-val2
    else:
        Result=val2-val1
elif op=='*':
    Result=val1*val2
elif op=='/':
    if val1>val2:
        Result=val1/val2
    else:
        Result=val2/val1
elif op=='%':
    Result=val1%val2
else:
    print("Enter any of the operator(+,-,*,/,%): ")
print("The operator ",op," between ",val1," and ",val2," is : ",Result)


    
