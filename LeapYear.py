'''WAP to check if a given year is a leap year or not using
#if-else statement'''
yr=int(input("Please Enter the year: "))
if ((yr%400==0)or (( yr%4==0 ) and (yr%100!=0))):
    print("%d is a Leap year" %yr)
else:
    print("%d is Not a Leap year" %yr)
