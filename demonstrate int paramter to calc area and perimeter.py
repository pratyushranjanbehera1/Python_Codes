#WAP to demonstrate the integer parameter to calculate area and perimter of a rectangle
def recarprcalc(l,b):
    ar=l*b
    pr=2*(l+b)
    return(ar,pr)
x=float(input("enter length of rectangle;"))
y=float(input("enter breadth of rectangle;"))
a,p=recarprcalc(x,y)
print(a)
print(p)
recarprcalc(x,y)
