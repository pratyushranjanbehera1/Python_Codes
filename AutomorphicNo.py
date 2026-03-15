#A number is said to be an automorphic number if the last digits of the square
#of this number give the same number. Ex The square of 25 gives 625,
#since the last digits are 25 it is an automorphic number.
num = int(input("Enter a number you want to check: \n"))    
num_of_digits = len(str(num))   
square=num**2     
last_digits=square%pow(10,num_of_digits)    
if last_digits==num:  
  print("Yes, {} is an automorphic number".format(num))  
else:  
  print("No, {} is not an automorphic number".format(num))

  
