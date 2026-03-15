# Python Program to Find LCM of Two Numbers using For loop
p,q,x,g=0,0,0,0
# p & q - To store the two positive numbers
# x - To store the LCM number
# g - To store the GCD
print ("-----Enter the two positive integer numbers-----")
p=int(input("Enter the first number:"))
q=int(input("Enter the Second number:"))
for i in range(1,p+1):
    if i<=q:
        if p%i==0 and q%i==0:
            g = i
x=(p*q)/g
print ("\nThe LCM of two positive numbers ", p, " & ", q, " is ", x, ".")

#OR
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
for i in range(max(num1, num2), 1 + (num1 * num2)):
    if i % num1 == i % num2 == 0:
        lcm = i
        print("LCM of", num1, "and", num2, "is", lcm)
        break


