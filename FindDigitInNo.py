#WAP to check whether a given digit is present in a given number or not.
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
