#WAPto assign some names in a list.Pass the list to a function and
#arrange the names in an alphabetical order by using 'Bubble Sort'
#technigue.Display the arranged names.
def Arrange(Nlist):
    size=len(Nlist)
    for i in range(size):
        for j in range(size):
            if Nlist[i]<Nlist[j]:
                temp=Nlist[i]
                Nlist[i]=Nlist[j]
                Nlist[j]=temp
    return Nlist
Mylist=["Rohit","Ajaya","Deepak","Sekhar","Vikash"]
print("The elements of the list is\n ",Mylist)
NewList=Arrange(Mylist)
print("The elements of the list in ascending order\n ",NewList)

                
