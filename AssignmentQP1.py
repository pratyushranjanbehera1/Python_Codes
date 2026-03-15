#Q1WAP to print thr statement "Learning is a part of Journey"
print("Learning is a part of Journey")
#Q2WAP to take your name,take input with the help of keyboard.
nm=input("Enter your name: ")
print("Your name is :",nm)
#Q3 WAP to take 2 numbers from the keyboard and print them
a=int(input("Enter the first number: "))
b=int(input("Enter the second number: "))
print("The first number you have entered is: ",a )
print("The second number you have entered is: ",b )
'''Q4 WAP to generate the following required output with the help of
arithematic operator
output 1:Addition of two numbers 20 and 5 is 25
outpot 2:Multiplication of two numbers 20 and 5 is 100
output 3: Modulus of two numbers 20 and 5 is 0
output 4: Exponent of two numbers 20 and 5 is 3200000'''
a=20
b=5
Sum=a+b
Mul=a*b
Modu=a%b
Expo=a**b
print("Addition of two numbers",a," and ",b," is ",Sum)
print("Multiplication of two numbers",a," and ",b," is ",Mul)
print("Modulus of two numbers",a," and ",b," is ",Modu)
print("Exponent of two numbers",a," and ",b," is ",Expo)
#Q5 WAP to print the first19 natural number in reverse order
for i in range(19,0,-1):
    print(i,end='')
#Q6 WAP that allows the user to convert temperature from Celsius to Fahrenhit or vice versaFar to Cel
celsius=int(input("Enter the temperature in celcius:"))
f=(celsius*1.8)+32
print("Temperature in farenheit is:",f)   
#Q7 WAP add those numbers whose last digit is 9 between 1 to 1000
Sum=0
for i in range(1,1001):
    if(i%9==0):
        Sum=Sum+i
print("Sum of the numbers is :",Sum)
#Q8 WAP to find the sum of all even numbers and all odd numbers
#seperately between 17 to 84
evenSum=0
oddSum=0
for i in range(17,85):
    if i%2==0:
        evenSum=evenSum+i
    else:
        oddSum=oddSum+i
print("Even sum is :",evenSum)
print("Odd sum is :",oddSum)
#Q9 WAP to accept 10 numbers from user and find their average
Sum=0
for i in range(1,11):
    x=int(input("Enter a number:"))
    Sum=Sum+x
print("The average of the number is :",Sum/10)
#Q10 WAP to check the given character is vowel or consonent
ch=input("accept a character: ")
if ch=='a' or ch=='e' or ch=='i' or ch=='o' or ch=='u' or ch=='A' or ch=='E' or ch=='I' or ch=='O' or ch=='U':
    print("you have antered vowel character")
else:
    print("You have entered consonent character")
#Q11 WAP to print even number between 2 to 20 using while loop
    i=2
    while i<20:
        print(i)
        i=i+2
#Q12 WAP to print the factorial of a number using a while loop
n=int(input("Enter a number: "))
fact=1
i=1
while(i<=n+1):
    fact=fact*i
    i=i+1
print("the factorial of the number is:",fact)
#Q13 WAP to check if a given year is a leap year or not using
#if-else statement
yr=int(input("Please Enter the year: "))
if ((yr%400==0)or (( yr%4==0 ) and (yr%100!=0))):
    print("%d is a Leap year" %yr)
else:
    print("%d is Not" %yr)
    
#Q14 WAP to accept any 3 number and find the largest of three
#    number using if else statement.
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
#Q15 WAP to count the number of digits in a given number
#    using while loop
n=int(input("Enter a number:"))
count=0
while n>0:
    count=count+1
    n=n//10
print("the number of digit in the number is ",count)

#Q16 WAP to find the sum and product of digits of a number
#inputed by user        
N=int(input("Enter any Number: "))
Prod=1
while(N>0):
    Rem=N%10
    Sum=Sum+Rem
    Prod=Prod*Rem
    N=N//10
print("Sum of the digits of Given Number:",Sum)
print("Multiplication of the digits of Given Number:",Prod)
#Q17 WAP to check whether a number is prime number or not
num=int(input("Enter a number: "))
if num > 1:
    for i in range(2, int(num/2)+1):
        if (num % i) == 0:
            print(num, "is not a prime number")
            break
    else:
        print(num, "is a prime number")
else:
    print(num, "is not a prime number")

#Q18 WAP to display the multiplication table of a given number
#in the format
n=int(input("Enter the table number: "))
for i in range(1,11):
    print(n,' x ',i,' = ',n*i)

#Q19 WAP to check whether a given digit is present in a given number or not.
n=int(input("Enter a number: "))
m=int(input("Enter the number to search: "))
num=n
for i in range(n):
    rem=n%10
    if rem==m:
        print(m," is found in ",num)
        break
    else:
        print(m," is not found in ",num)
        break
    n=n//10
#Q20 WAP to print all the prime numbers between 1 to 100
N=1
while(N<=100):
    count=0
    i=2
    while(i<=N//2):
        if(N%i==0):
            count=count+1
            break
        i=i+1
    if(count==0 and N!=1):
        print("%d"%N,end=' ')
    N=N+1
'''#Q21WAP to enter the marks of 4 subject and calculate the grade
of a student based on the average marks using if-else statement
if total marks > 90 then grade A
and total marks > 80 then grade B
and total marks > 70 then grade C
and total marks > 60 then grade D
other than that grade E'''
sub1=int(input('enter mark of subject1='))
sub2=int(input('enter mark of subject2='))
sub3=int(input('enter mark of subject3='))
sub4=int(input('enter mark of subject4='))
avg=(sub1+sub2+sub3+sub4)/4
if avg>90:
    print("Grade-A")
elif avg>80:
    print("Grade-B")
elif avg>70:
    print("Grade-C")
elif avg>60:
    print("Grade-D")
else:
    print("Grade-E") 

#Q22 WAP to check the inputted number is palindrome numbers or not.
n=int(input("Enter number:"))
temp=n
rev=0
while(n>0):
 dig=n%10
 rev=rev*10+dig
 n=n//10
if(temp==rev):
 print("The number is a palindrome!")
else:
 print("The number isn't a palindrome!")
#Q23 WAP to enter two number and find the value of one number is
#the power of another
a=int(input("Enter first number: "))
b=int(input("Enter second number: "))
print("The value of ",a,"to the power",b," is ",a**b)
#Q24 WAP to reverse a number and print it.
n=int(input("Enter number: "))
rev=0
while(n>0):
    dig=n%10
    rev=rev*10+dig
    n=n//10
print("Reverse of the number:",rev)
#25 WAP to find the LCM of two given numbers
p,q,x,g=0,0,0,0
# p & q - To store the two positive numbers
# x - To store the LCM number
# g - To store the GCD
p=int(input("Enter the first number:"))
q=int(input("Enter the Second number:"))
for i in range(1,p+1):
    if i<=q:
        if p%i==0 and q%i==0:
            g=i
x=(p*q)/g
print("\nThe LCM of two positive numbers ", p, " & ", q, " is ", x, ".")
#Q26 WAP that generates the Fibonacci sequence up to a given number
#entered by user using a loop
n=int(input("Enter the number of terms: "))  
n1=0  
n2=1  
print("The fibonacci sequence of the numbers is:")
print(n1)
print(n2)
for i in range(1,n-1,1):
    sum=n1+n2
    print(sum)
    n1=n2
    n2=sum
#Q27 WAP that allow the user to enter a number and check whether it
#is an armstrong number or not.
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
'''Q28 WAP program to generate the given pattern:
*****
*****
*****
'''
i=1
while i<=3:
    j=1
    while j<=5:
        print("*",end="")
        j=j+1
    i=i+1
    print()
#Q29 WAP to check if a given number is positive,negative or zero
#using if-else statement.
num=int(input("Enter a number: "))
if num==0:
 	print("The number is zero")
elif num>0:
 	print("The number is +ve")
else:
 	print("The number is -ve")
#Q30 WAP to check if a given string is palindrome or not
#using if-else statement.
str=input("Enter string: ")
if(str==str[::-1]):
    print("The string is a palindrome.")
else:
 print("The string is not a palindrome.")




 

    
    
        


    




    
    
    










        
        



    


#






      



