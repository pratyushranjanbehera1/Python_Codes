#WAPP program to check if the given number is Happy Number
#A number is said to be happy if it yields 1 when replaced by the sum of squares of its digits repeatedly.
#If this process results in an endless cycle of numbers containing 4, then the number will be an unhappy number.
#Number = 32
#32+ 22 = 13
#12 + 32 = 10
#12 + 02 = 1
#isHappyNumber() will determine whether a number is happy or not    
def isHappyNumber(num):    
    rem=sum=0    
    while(num>0):    
        rem=num%10;    
        sum=sum+(rem*rem);    
        num=num//10;    
    return sum;    
num=int(input("Enter a number:"))    
result=num;    
while(result!=1 and result!=4):    
    result=isHappyNumber(result); #Happy no. always ends with 1    
if(result==1):    
    print(str(num) + " is a happy number");    
#Unhappy no. ends in a cycle of repeating numbers which contain 4    
elif(result==4):    
    print(str(num)+ " is not a happy number");   
