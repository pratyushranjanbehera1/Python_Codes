'''PROGRAM TO PRINT THE LARGEST AND SMALLEST NUMBER FROM A LIST'''
li=eval(input('Enter a list of numbers:'))
g=s=li[0]
l=len(li)
for i in range(l):
    if li[i]>g:
        g=li[i]
    if li[i]<s:
        s=li[i]
print('Largest no=',g)
print('Smallest no=',s)
