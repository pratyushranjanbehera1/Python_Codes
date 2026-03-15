#WAP to calculate the volume of a cuboid using function
#With positional argument
def volume(l,b,h):
    vol=0
    vol=l*b*h
    return vol
m=int(input("Enter the length:"))
n=int(input("Enter the breadth:"))
p=int(input("Enter the height:"))
v=volume(m,n,p)
print("Length is",m,",Breadth is ",n,"and height is ",p)
print("volume is ",v)
