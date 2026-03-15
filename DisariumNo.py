#WAPP to check if the given number is a Disarium Number 175=1+7**2+5**3,89,135
n=input("Enter a number:-")
len_n=len(n)
n=int(n)
num=n
sum=0
i=len_n
while(n!=0):
    rem=n%10
    sum=sum+pow(rem,i)
    n=int(n/10)
    i=i-1
if(sum==num):
    print("Disarium Number!")
else:
    print("Not a Disarium Number!")
