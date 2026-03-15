#WAP to accepta string and display the number of vowel present in
#it using function.
def vowelCount():
    str=input("Enter a string:")
    vowel=0
    for i in str:
        if i in "aeiouAEIOU":
            vowel=vowel+1
    print("Number of vowel present in the string",vowel)
vowelCount()
