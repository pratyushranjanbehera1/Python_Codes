#WAP to count total number vowel & consonent present in a string
str=input('Enter a string:')
Vc=0
Cc=0
for i in str:
    if (i>='a' and i<='z')or(i>'A' and i<='Z'):
        if i in('a','e','i','o','u','A','E','I','O','U'):
            Vc=Vc+1
        else:
            Cc=Cc+1
print('No. of Vowels in the String=',Vc)
print('No. of Consonents in the String=',Cc)

#OR alternate method
#WAP to Count Vowels and Consonants in a String
str1=input("Please Enter Your Own String : ")
vowels=0
consonants=0
for i in str1:
    if(i=='a' or i=='e'or i=='i' or i=='o' or i=='u' or i=='A' or i=='E' or i=='I' or i=='O' or i=='U'):
        vowels=vowels+1
    else:
        consonants = consonants+1
print("Total Number of Vowels in this String = ", vowels)
print("Total Number of Consonants in this String = ", consonants)
