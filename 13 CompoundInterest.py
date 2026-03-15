#Write a Python program to Calculate Compound Interest.
#CI=PrincipalAmount*(1+ROI)**NumberOfYears)
import math
P=float(input("Enter the Principal Amount : "))
R=float(input("Enter the Rate Of Interest : "))
T=float(input("Enter Time period in Years : "))
CI_future=P*(math.pow((1+R/100),T)) 
CI= CI_future-P
print("Future Compound Interest for Principal Amount {0}= {1}".format(P,CI_future))
print("Compound Interest for Principal Amount {0}={1}".format(P,CI))
