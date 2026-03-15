#WAPP to Print the Fibonacci sequence
nterms=int(input("How many terms the user wants to print? "))  
#First two terms  
n1=0  
n2=1  
count=0  
#Now, we will check if the number of terms is valid or not  
if nterms<=0:  
    print("Please enter a +ve integer,the given no. is not valid")  
#if there is only one term, it will return n1  
elif nterms==1:  
    print("The Fibonacci sequence of the Nos. up to",nterms,": ")  
    print(n1)  
#Then we will generate Fibonacci sequence of number  
else:  
    print("The fibonacci sequence of the numbers is:")  
    while count<nterms:  
        print(n1)  
        sum=n1+n2  
       #At last, we will update values  
        n1=n2  
        n2=sum  
        count=count+1  
