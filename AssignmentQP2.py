#Q1WAP to count the no of characters in a string input by user
str=input("Enter a string:")
count=0
for i in str:
    count=count+1
print("The number of character is ",count)

#Q2 WAP to  reverse a string(should take by user input)
#and check if that string is palindrome or not.
str=input("Enter a string:")
rev=str[::-1]
print("original string is ",str)
print("Reverse string is ",rev)
if rev==str:
    print(str,"is a palindrome")
else:
    print(str,"is not a palindrome")
#Q3 WAP to take two strin taken from keyboard
str1=input("Enter the first string")
str2=input("Enter the second String")
MergStr=str1+str2
print("the mearge string is ",MergStr)
#Q4 WAP to split a string into a list of words
str=input("Enter a string to split:")
print(str.split())

#Q5 WAP to find the sum of all elements in a list.
#(list should be taken by user input)
lst=[]
sum=0
x=int(input("Enter size of the list"))
for i in range(x):
    l=int(input("Enter the element of the list"))
    lst.append(l)
print("the list is:",lst)   
for i in range(len(lst)):
    sum=sum+lst[i]
print("The sum of the elements is:",sum)

#Q6 WAP to find out the maximum and minimum value of a list
lst=[]
sum=0
x=int(input("Enter size of the list"))
for i in range(x):
    l=int(input("Enter the element of the list"))
    lst.append(l)
print("the list is:",lst) 
print("The maximum value in the list",max(lst))
print("The minimum value in the list",min(lst))
#Q7 WAP to sort a list in asscending order
#(list should be inputed by user)
lst=[]
sum=0
x=int(input("Enter size of the list"))
for i in range(x):
    l=int(input("Enter the element of the list"))
    lst.append(l)
print("the list is:",lst)
print("After sorting")
lst.sort()
print(lst)
#Q8 WAP to remove duplicate from the list
lst=[]
sum=0
x=int(input("Enter size of the list"))
for i in range(x):
    l=int(input("Enter the element of the list"))
    lst.append(l)
print("the list is:",lst)
print(list(set(lst)))
'''Q9 WAP to create an empty list and pass this given information
to the list
Name,age,id,Address
Input:Name:Rohan
Input:Age:19
Input:id:23mdsa25
Input:Address:Patia
output:["Rohan",19,"23msda25","patia"]'''
name=input("Enter name")
age=int(input("Enter age "))
id=input("Enter id")
address=input("Enter address")
student=[name,age,id,address]
print(student)
#Q10 WAP in python to reverse a list.
l=[]
n=int(input("Enter List size :"))
for i in range(n):
x=int(input("Enter element"))
l.append(x)
print("Reverse of the list is :",[::-1])
#Q11 Write a program to check if two lists are equal or not.
#(the list should be inputted)
lst1=eval(input("Enter value for first list "))
lst2=eval(input("Enter value for first list "))
if lst1==lst2:
    print("Equal list")
else:
    print("Not equal list")
#Q12 Write a program in python to find the second largest value in a list. (the list sho
lst=[]
n=int(input("Enter list size :"))
for i in range(n):
    x=int(input("Enter element :"))
    lst.append(x)
s1=s2=lst[0]
for i in range(1,n):
    if lst[i]>s1:
        s2=s1
        s1=lst[i]
    elif lst[i]== s1:
        pass
    else:
        if lst[i]>s2:
            s2=lst[i]
print("List is :",lst)
print("Second largest element=",s2)
#Q13 WAPP to find the length of a tuple. Input: tpl1=(1, 2, 3,4,5)
t=(1,2,3,4,5)
print("Length of the tuple = ",len(t))
#Q14 WAP to access element of a touple my_element=(1,2,3,4,5)
t=eval(input(“ Enter a tuple”))
p=int(input(“ Enter the position “)
if p>=len(t):
      print (“ index out of range ”)
else:
    print(t[p])
#Q15 WAP to check if an element exists in a tuple
t=()
n=int(input("Enter no of element :"))
for i in range(n):
x=int(input("enter element :"))
t=t+(x,)
val=int(input("Enter value to search :"))
if val in t:
    print("Exist in the tuple")
else:
    print("Element does not exist")
#Q16 Create a list of length 8 and pass the elements at given index. List[1]=2; List[4]=
#Input: list[1,3,4,5,6,8,9]
#Output: [1,2,4,5,7,8,9]
lst=[1,2,3,4,5,6,7,8]
lst[1]=2
lst[4]=7
print(lst)
#Q17 Write a program in python to access the value of a specific key in a dictionary.
my_dict={'name':'John','age':25,'city':'Bhubaneswar'}
x=input("Enter the key value")
for i in my_dict:
    if i==x:
        print("Required :",i,"=",my_dict[i])
#Q18 WAP in python to check if a key exists in a dictionary.
#my_dict = {'name': 'John', 'age': 25, 'city': 'Bhubaneswar'}
#Input: Enter the key: city
#Output: Yes, that exists
my_dict={'name':'John','age':25,'city':'Bhubaneswar'}
x=input("Enter the key :")
for i in my_dict:
    if i==x:
        print(" Yes , That exists")
#Q19 WAP python to find the length of a dictionary.
#my_dict={'name':'John','age':25,'city':'Bhubaneswar'}
# Output: Length of the dictionary: 3
my_dict={'name':'John','age':25,'city':'Bhubaneswar'}
print("Length=",len(my_dict))
#Q20 Write a program in python to add a new key-value pair to a dictionary and remove
#a key-value pair from a dictionary.
a={1:"A",2:"B",3:"C"}
b={10:"Ram",2:"HARI",4:"BINOD"}
a.update(b)
print(a)
#Q21 WAP in python to merge two dictionaries.
a={1:"A",2:"B",3:"C"}
b={10:"Ram",2:"HARI",4:"BINOD"}
a.update(b)
print(a)
#Q22 WAP to sort the elementof a list(user input) and remove
#the duplicate(using set).
Lst=[5,1,9,3,1,7,8,5,6]
L=set(Lst)
print(L)
#Q23 WAP to add an element to a set and remove an element from a set
#my_set={1, 2, 3, 4, 5}
s=set()
ele=input("Enter the element you want to add:-")
s.add(ele)
print("Resultant set=",s)
ele=input("Enter the element you want to remove:-")
s.remove(ele)
print("Resultant set=",s)

#Q24 WAP to printthe value of tuple by using iter()
#method with the given tuple
T=(1,2,3,4,5)
T1=iter(T)
print(next(T1),end=" ")
print(next(T1),end=" ")
print(nex(T1),end=" ")

#Q25 Create a list using list comprehension consisting of all
#even number from the range 0 to 20.
L=[]
for i in range(0,20,2):
    L.append(i)
print(L)

#Q26 WAP to find the area of a triangle from its three sides by the
#help of lambda function
import math
s=lambda x,y,z:(x+y+z)/2
ar=lambda s,x,y,z:
math.sqrt(s*((s-x)*(s-y)*(s-z)))
s1=float(input("Enter side1:-"))
s2=float(input("Enter side2:-"))
s3=float(input("Enter side3:-"))
a=s(s1,s2,s3)
b=ar(a,s1,s2,s3)
print(b)
#Q27 WAP to find the area of a circle, by using lambda function.  
a=lambda r:3.14*r**2
r=float(input("Enter radius:-"))
print("Area=",a(r))
#Q28 WAP by using function for addition,sub,mult,div etc and show it.
def add(n1,n2):
    return n1+n2
def sub(n1,n2):
    return n1-n2
def mul(n1,n2):
    return n1*n2
def div(n1,n2):
    return n1/n2
print("1 For addition\n2 For subtraction\n3 For multiplication\n4 or division")
ch=int(input("Enter the option:"))
n1=int(input("Enter first number:-"))
n2=int(input("Enter second number:-"))
if ch==1:
    print("Addition=",add(n1,n2))
elif ch==2:
    print("Subtraction=",sub(n1,n2))
elif ch==3:
    print("Multiplication=",mul(n1,n2))
elif ch==1:
    print("Division=",div(n1,n2))
else:
    print("Invalid input")
#Q29 WAP to print the employee detailwith the help of function,and
    #by-passing argument to the function.
def Prin(n,a,id,sal):
    print("name=",n)
    print("Address",a)
    print("ID=",id)
    print("Salary",sal)
nm="RAM"
add="Patia"
id="1111"
sal=45000
Prin(nm,add,id,sal)
# Q30 Write a program to perform various operations on sets (e.g., union, intersection, d
Input:
    Enter elements for the first set(space-separated):10 20 30 40
    Enter elements for the second set(space-separated):50 60
Display:
    Set1: {'40','10','30','20'}
    Set2:{'50','60'}
Input:Enter the operation to perform (union,intersection,difference):
union Final Output:Result: {'30','60','10','40','50','20'}














           
