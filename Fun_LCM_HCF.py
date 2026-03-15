#WAP to calculate the HCF and LCM  by accept two number from
#the user.use the function to return HCF of the number
#LCM=A*B/HCF
def HCF(n1,n2):
    a,b=n1,n2
    p=a*b
    for i in range(1,p):
        if((a%i==0) and (b%i==0)):
            gcd=i
    return gcd
m=int(input("Enter first number"))
n=int(input("Enter second number"))
k=HCF(m,n)
lcm=int(m*n)/k
print("The GCD/HCF of two number is ",k)
print("The LCM of the two number is ",lcm)
