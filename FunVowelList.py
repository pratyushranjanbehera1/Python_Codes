#WAP to store all vowel from a string in to a list using function
#and display the list after.
def vowelList():
    vowel=[]
    NVowel=[]
    str=input("Enter a string:")
    for i in range(0,len(str)):
        if str[i] in "aeiouAIEOU":
            vowel.append(str[i])
        else:
            NVowel.append(str[i])
    print("List of Vowels is ",vowel)
    print("List of New Vowels are",NVowel)
vowelList()

            
