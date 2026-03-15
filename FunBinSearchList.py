#WAP to search an element in the list by using
#Binary Search Technique.using function.
def BinSearch(NList):
    num=eval(input("Enter the element to be searched "))
    flag=False
    p=len(NList)
    first=0
    last=p-1
    while(first<=last):
        mid=int((first+last)/2)
        if(NList[mid]==num):
            flag=True
            break
        if(num<NList[mid]):
            last=mid-1
        if(num>NList[mid]):
            first=mid+1
    return flag
MyList=eval(input("Enter a set of sorted numbers in the list:"))
print("Element of the list:",MyList)
fg=BinSearch(MyList)
if(fg==True):
    print("Searching number is in the list")
else:
    print("Searching number is not in the list")
    



      
