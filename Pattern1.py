'''Pattern #1: Simple Number Triangle Pattern
Pattern:

1  
2 2  
3 3 3  
4 4 4 4  
5 5 5 5 5
'''
rows=int(input("Enter the number of rows+1: "))
for i in range(rows):
    for j in range(i):
        print(i, end=' ') # print number
    #line after each row to display pattern correctly
    print(' ')
