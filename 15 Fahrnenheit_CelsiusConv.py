#Python Program to Convert Celsius to Fahrenheit
celsius=int(input("Enter the temperature in celcius:"))
f=(celsius*1.8)+32
print("Temperature in farenheit is:",f)

#WAPP To Convert Degree Fahrenheit into Degree Celsius
Fahrenheit_1 = float( input("Temperature value in degree Fahrenheit: " ))  
# For Converting the temperature from degree Fahrenheit to degree Celsius   
celsius_1 =(Fahrenheit_1-32)/1.8  
# Print the result  
print ('The %.2f degree Fahrenheit is equal to: %.2f Celsius'%(Fahrenheit_1, celsius_1))  
  
print("----OR----")  
Fahrenheit_2=float(input("Temperature value in degree Fahrenheit: " ))  
celsius_2=(Fahrenheit_2-32)*5/9  
# Print the result  
print ('The %.2f degree Fahrenheit is equal to: %.2f Celsius'%(Fahrenheit_2, celsius_2))  


#WAPP to convert the temperature into Celsius to Fahrenheit T(°Fahrenheit)=(T(°Celsius)*1.8)+32 or T(°Fahrenheit)=(T(°Celsius)*9/5)+32
celsius_1=float(input("Temperature value in degree Celsius: " ))  
# For Converting the temperature to degree Fahrenheit by using the above given formula  
Fahrenheit_1=(celsius_1*1.8)+32  
# print the result  
print('The %.2f degree Celsius is equal to: %.2f Fahrenheit'%(celsius_1,Fahrenheit_1))  
print("----OR----")  
celsius_2=float(input("Temperature value in degree Celsius: "))  
Fahrenheit_2=(celsius_2*9/5)+32      
# print the result  
print('The %.2f degree Celsius is equal to: %.2f Fahrenheit'%(celsius_2,Fahrenheit_2))  
