#WAP to display the series 1 2 4 7 11....n
n=int(input("Enter the number of terms: "))
first=1
second=0
for i in range(0,n+1):
    first=first+second
    print(first)
    second=second+1
    
