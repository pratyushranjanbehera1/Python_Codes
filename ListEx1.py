'''WAP to create a list  of five natural number and display
the even number
L1=[1,2,3,4,5]
for i in L1:
    if i%2==0:
        print(L1[i])'''

Li=[i*1 for i in range(5) if i%2==0]
print(Li)
