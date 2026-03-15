'''PROGRAM TO FIND THE POSITION OF AN ELEMENT FROM A LIST'''
lis=eval(input('Enter elements for the list:'))
s=int(input('Enter element to search from the list:'))
L=len(lis)
pos=-1
for i in range(L):
    if lis[i]==s:
        pos=i
        break
if pos==-1:
    print('Element not found in List')
else:
    print('Position of the element=',pos)
