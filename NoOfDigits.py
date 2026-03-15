#WAP to count the no.of digits in a given number using while loop
n=int(input("Enter a number:"))
count=0
while n>0:
    rem=n%10
    count=count+1
    n=n//10
print("the number of digit in the number is ",count)
