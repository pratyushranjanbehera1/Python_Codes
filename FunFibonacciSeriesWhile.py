#WAP to generate the fibonacci series up to n terms,pass the value
#of n to a function and display all the numbers of the sries in the
#function as a list element.
def fibonacci(n):
    result=[]
    a,b,c=-1,1,0
    while c<n:
        c=a+b
        result.append(c)
        a=b
        b=c
        c=a+b
    return result
n=int(input("Enter the value of n"))
f=fibonacci(n)
print("Fibonacci series upto ",n,"is")
print(f)
