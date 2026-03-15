#WAPP to Find Armstrong Number between an Interval
lower=int(input("Enter lower range: "))  
upper=int(input("Enter upper range: "))  
for num in range(lower,upper + 1):  
   sum=0  
   temp=num  
   while temp>0:  
       rem=temp%10  
       sum=sum+rem**3  
       temp=temp//10  
       if num==sum:  
            print(num)  
