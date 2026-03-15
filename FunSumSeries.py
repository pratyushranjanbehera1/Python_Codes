#WAP to find the sum of the series using function
#s=1*2+2*3+3*4+....+19*20
def prod(n1,n2):
    c=n1*n2
    return c
s=0
for i in range(1,20):
    p=prod(i,i+1)
    s=s+p
print("The sum of the series ",s)

