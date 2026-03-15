#WAP to replace vowel by "a" and count the vowel of the inputed
#string using function.
def VowelReplaceCount():
    a=0
    str=input("Enter a string:")
    for i in range(0,len(str)):
        if str[i]in "aeiouAEIOU":
            str=str.replace(str[i],"a")
            a=a+1
    print("After replacing the vowels the string is ",str)
    print("The No. of vowel characters present in the string is",a)
VowelReplaceCount()
