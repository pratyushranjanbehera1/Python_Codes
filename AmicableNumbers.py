'''Two different numbers are said to be so Amicable Numbers if each sum of
divisors is equal to the other number.Amicable Numbers are:
(220,284),(1184,1210),(2620,2924),(5020,5564),(6232,6368) etc.
Ex– 220 and 284 are Amicable Numbers.
Divisors of 220=1,2,4,5,10,11,20,22,44,55,110
1+2+4+5+10+11+20+22+44+55+110=284
Divisors of 284=1,2,7,71,142
1+2+7+71+142=220'''
x=int(input('Enter number 1: '))
y=int(input('Enter number 2: '))
sum1,sum2=0,0
for i in range(1,x):
    if x%i==0:
        sum1+=i
for j in range(1,y):
    if y%j==0:
        sum2+=j
if(sum1==y and sum2==x):
    print('Amicable!Number')
else:
    print('Not Amicable! Number')
    
