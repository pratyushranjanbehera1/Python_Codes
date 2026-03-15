#WAP to accept a line and give the statsics of Uppercase letter,
# lower case letter,no of alphabets,and digits
line=input("Enter a line ")
lowerCount=0
upperCount=0
alphaCount=0
digitCount=0
for i in line:
    if i.islower():
        lowerCount=lowerCount+1
    elif i.isupper():
        upperCount=upperCount+1
    elif i.isdigit():
        digitCount=digitCount+1
    if i.isalpha():
        alphaCount=alphaCount+1
    
print("Number of Uppercase letter: ",upperCount)
print("Number of Lowercase letter: ",lowerCount)
print("Number of alphabet letter: ",alphaCount)
print("Number of digits : ",digitCount)
