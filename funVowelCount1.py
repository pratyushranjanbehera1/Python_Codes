#WAP to accept a word in a mixed case and pass it to a function
#the function should count the number of vowels present in the
#given string and returns the number of vowels to the main program.
def Vowels(str):
    vowels="aeiouAEIOU"
    c=0
    p=len(str)
    for i in range(0,p):
        if str[i] in vowels:
            c=c+1
    return c
nstr=input("Enter a string in sentance case")
v=Vowels(nstr)
print("The number of vowels in the string is ",v)
