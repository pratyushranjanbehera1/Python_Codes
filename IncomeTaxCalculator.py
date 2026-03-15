'''WAP to calculate the income tax of an employee on the basis of
basic salary and total savings inputed by the userusing nested if...
else statement as per the given slabs
* No tax for individual income <rs. 2.5 lacs
* 0%-5% tax with income Rs 2.5 - Rs 5 lacs for different age group
* 20% tax with income Rs 5- Rs 10 lacs
* investment upto rs 1.5lacs under section 80c can save upto
  Rs.45000 in tax'''

Basic=int(input("Enter the basic salary of the employeein Rupees: "))
Saving=int(input("Enter the total saving in Rupees: "))
if Basic<=250000:
    Tax=0
elif Basic<=500000: #Accessing the maximum saving limits
    if Saving>150000:
        Saving=150000
    Tot_Income=Basic-Saving-250000 #Total taxable income afterall the deductions
    Tax=Tot_Income*0.05 #Total Tax after calculation
elif Basic<=1000000:
    if Saving>150000:
        Saving=150000
    Tot_Income_5Slab=500000-Saving-250000 #Total income under 5% slab
    Tot_Income_20Slab=Basic-500000 #Total income under 20% slab
    Tax=Tot_Income_5Slab*0.05+Tot_Income_20Slab*0.02
else:
    if Saving>150000:
        Saving=150000
    Tot_Income_5Slab=500000-Saving-250000 #Total income under 5% slab
    Tot_Income_30Slab=Basic-1000000 #Total income under 30%slab
    Tax=Tot_Income_5Slab*0.05+Tot_Income_30Slab*0.03+100000 #100000 is for 20% slab
print("Total Income Tax to be paid= ",Tax) #50000 to 100000 tax calculated

