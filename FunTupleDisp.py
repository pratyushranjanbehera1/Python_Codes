#WAP to pass tuple to a function containing some words and
#disply the words start with vowel
def Vowel(NTuple):
    print("The words starting with vowels are ")
    vowels="aeiouAEIOU"
    for i in NTuple:
        if(i[0] in vowels):
            print(i)
    return
MyTuple=eval(input("Enter some words in a tuple\n"))
Vowel(MyTuple)
