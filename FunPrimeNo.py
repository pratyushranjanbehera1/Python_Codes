#WAP to accept a number pass it to a function which returns its
#number of factors.finally display whether the number is prime or
#not.
def Prime(n1):
    c=0
    n=n1
    for i in range(1,n+1):
        if (n%i==0):
            c=c+1
    return c
n=int(input("Enter a number"))
p=Prime(n)
if(p==2):
    print(n,"is a prime number")
else:
    print(n,"is not a prime number")
    

            
    
          
