'''PROGRAM TO DISPLAY ALL EVEN NUMBERS FROM A LIST'''
lis=eval(input('Enter elements for the list:'))
l=len(lis)
print('All even numbers in List are:')
for i in range(l):
    if lis[i]%2==0:
        print(lis[i],end=' ')
