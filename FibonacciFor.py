#WAPP to Print the Fibonacci sequence 0 1 1 2 3 5 8 13 ......n
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
