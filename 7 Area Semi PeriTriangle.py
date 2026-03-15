#WAPP to calculate the Area and semi perimeter of a triangle = (s*(s-a)*(s-b)*(s-c))-1/2
# Three sides of the triangle is a, b and c:  
a=float(input('Enter First Side: '))  
b=float(input('Enter Second Side: '))  
c=float(input('Enter Third Side: '))  
s=(a+b+c)/2 #calculate the semi-perimeter  
area=(s*(s-a)*(s-b)*(s-c))**0.5 #calculate the area
print("The semi-Perimeter of the triangle is :",s)
print('The area of the triangle is ',area)

