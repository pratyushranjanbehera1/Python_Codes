'''WAP to input a string and check if it is a palindrome string
or no using  a string slice'''
s=input("Enter a string :")
if s==s[::-1]:
    print("Palindrome string")
else:
    print("Not a palindrome String")
