#WAP to accept a word in lowercase and pass it to a function.
#Arrange all the letters of the word in its alphabetical order
#and display the result.
def Arrange(wd):
    p=len(wd)
    word=""
    for i in range(65,91):
        for j in range(0,p):
            ch=wd[j]
            if(ch==chr(i)or ch==chr(i+32)):
                word=word+ch
    return word
wd=input("Enter a word lowercase:")
wd=wd.lower()
wd1=Arrange(wd)
print("Dictionary Order:")
print(wd1)
