#WAP to check whether a inputed number is Harshad number or not
#examples: 153, 156, 24 etc.153 is Harshad number becuase it is divisible by
#1+5+3=9 i.e. 153/(1+5+3) = 153/9 = 17.
num=int(input('Enter number: '))
n=num
sum=0
while num:
    rem=num%10
    sum=sum+rem
    num//=10
if n%sum==0:
    print('%d is Harshad Number'%(n))
else:
    print('%d is Not Harshad Number'%(n))
