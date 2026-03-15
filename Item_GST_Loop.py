'''WAP to calculate the total amount payable by the customer on
purchase of any item with GST leived on it.'''
Choice='y'
Total=0.0
while Choice=='y' or Choice=='Y':
    Item_Price=int(input("Enter the Item Price: "))
    GST=int(input("Enter the GST on Item: "))
    Total=Total+(Item_Price+(Item_Price*GST)/100)
    Choice=input("Press Y to Continue else press any other key: ")
print("Total amount to be paid:",Total)
