'''WAP to accept a string and check the following
Alphanumeric,Aplhabet only,number only,Space,Upper case,lower case,
convert to lower case,convert to upper case'''
s=input("Enter a string ")
if s.isalnum():
    print(s,"contains alphanumeric data")
if s.isalpha():
    print(s,"contains alphabet data")
else:
    print(s,"not contains alphabet data")
'''if s.isdigit():
    print(s,"contains digits data")
if s.islower():
    print(s,"contains lower case data")
if s.isupper():
    print(s,"contains uppercase data")
if s.lower():
    print(s,"convert to lower case")
if s.upper():
    print(s,"convert to upper case")'''





    
