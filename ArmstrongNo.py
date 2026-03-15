#WAP to check whether the given number is armstrong or not without using power function
n=int(input("Enter a number : "))
num=n
b=len(str(n))
sum=0
while n!=0:
    rem=n%10
    sum=sum+(rem**b)
    n=n//10
if num==sum:
    print("The number ",num," is an armstrong number")
else:
    print("The number ",num," is not an armstrong number")
