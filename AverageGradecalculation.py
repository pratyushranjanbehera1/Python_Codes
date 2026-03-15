# wapp to accept 5 subject mark and calculate the total, avg, grade ,
#the grade range avg >90, Grade-A
#               avg >80&<=90, Grade -B
#               avg>70&<=80,Grade -C
#               avg>60&<=70,Grade-D
#               avg>50&<=60,Grade-Pass
#               else fail
M1=int(input("Enter english mark"))
M2=int(input("Enter Math mark"))
M3=int(input("Enter phyics mark"))
M4=int(input("Enter Chemistry mark"))
M5=int(input("Enter Biology mark"))
total=M1+M2+M3+M4+M5
avg=total/5
print("Total Score=",total)
print("Average Score=",avg)
if avg>90:
    print("Grade Scored-A")
elif avg>=80:
     print("Grade Scored-B")
elif avg>=70:
     print("Grade Scored-C")
elif avg>=60:
     print("Grade Scored-D")
elif avg>=50:
     print("Grade Scored-Pass")
else:
     print("Grade Scored-Fail")
