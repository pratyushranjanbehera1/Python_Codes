#Creating a two dimensional List
lst=[ ]
r=int(input('How many rows:'))
c=int(input('How many columns:'))
for i in range(r):
    row=[ ]
    for j in range(c):
        value=int(input('Value for index '+str(i)+str(j)+':'))
        row.append(value)
    lst.append(row)
print(lst)
