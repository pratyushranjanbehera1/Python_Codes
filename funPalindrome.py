#WAP to accept a word and pass it to a funtion. The function checks
#whether it is a palindrome or not.
def Palin_Word(word):
    wd1=word
    if(wd1[::1]==wd1):
        k=1
    else:
        k=0
    return k
wd=input("Enter a word in uppercase:")
wd=wd.upper()
p=Palin_Word(wd)
if(p==1):
    print("Palindrome Word")
else:
    print("Not a Palindrome Word")
