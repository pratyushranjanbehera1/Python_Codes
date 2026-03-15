#WAP to accept a number and check whether it is an armstrong number or not.
num=int(input("Enter a number: "))
sum=0
n=num
while num>0:
    rem=num%10
    sum=sum+rem**3
    num=num//10
if n==sum:
    print(n,"is an Armstrong number")
else:
    print(n,"is not an Armstrong number")

