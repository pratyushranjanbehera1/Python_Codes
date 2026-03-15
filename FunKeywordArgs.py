#WAP to demonstrate the Keyword argument using function
def Surface_ar(l,b,h):
    print("length=",l)
    print("Breadth=",b)
    print("Height=",h)
    ar=2*(l*b+b*h+h*l)
    print("surface area is ",ar)
    return
Surface_ar(b=12,h=10,l=20)
    
