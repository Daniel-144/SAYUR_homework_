# to calculate the the income tax for an individual based on each tax slab.
"""""
income tax calculation based on the old tax regime.
according to old regime everyone are categorized based on their ages.
*age<60 - citizen category.
*age>60 and age<=80 - senior citizen category.
*age>80 -super senior citizen category.
tax based on category
      citizen                              |      senior citizen                       |   super senior citizen                      |
taxable income: 2.5l- tax=0                |taxable income<=300000- tax=0              |taxable income<=500000- tax=0                |
taxable income: 250000 to 500000 - tax=5%  |taxable income: 300000 to 500000 - tax=5%  |taxable income: 500000 to 10000000 -tax=20%  |
taxable income: 500000 to 1000000- tax=20% |taxable income: 500000 to 10000000 -tax=20%|taxable income>1000000 - 30%                 |
taxable income> 1000000 - tax=30%          |taxable income>1000000  - 30%              |
"""

gross_salary = float(input("enter your gross salary: "))
deductions = float(input('enter the deductions: '))
# subract deductions from gross salary to find the taxable income
taxable_income = gross_salary-deductions
age = int(input("enter your age (age should be greater than 16):"))
cumulative_tax = 0
tax_after_10l=0.3
# to calculate the tax for age>60
if age<60:
    # tax percentages 
    tax_percentage = [0,0.05,0.2,0.3]
    #tax slabs(the last element of the slab is taxable income because there is no slabs greater than 10l)
    slab=[250000,500000,1000000,taxable_income]
    print("category: citizen")
    for i in range(0,len(slab)):
        if taxable_income <= slab[i]:
            if(i==0):
              cumulative_tax = taxable_income * tax_percentage[i]
              i+=1
            else:
              cumulative_tax += (taxable_income-slab[i-1])*tax_percentage[i]
              print(slab[i]-slab[i-1])
            break
        else:
            if(i==0):
              cumulative_tax += slab[i] * tax_percentage[i]
            else:
               cumulative_tax += (slab[i]-slab[i-1])*tax_percentage[i]
    print("taxable income:",taxable_income)
    print("income tax:",cumulative_tax)
# for age from 60 t0 80
elif(age >= 60 and age<=80):
   # tax percentage
   tax_percentage = [0,0.05,0.2,0.3]
   #tax slabs(the last element of the slab is taxable income because there is no slabs greater than 10l)
   slab=[300000,500000,1000000,taxable_income]
   print("category: 'senior citizen'")
   for i in range(0,len(slab)):
        if taxable_income <= slab[i]:
            if(i==0):
              cumulative_tax = taxable_income * tax_percentage[i]
              i+=1
            else:
              cumulative_tax += (taxable_income - slab[i-1])*tax_percentage[i]
            break
        else:

            if(i==0):
              cumulative_tax += slab[i] * tax_percentage[i]
            else:
               cumulative_tax += (slab[i]-slab[i-1])*tax_percentage[i]
   print("taxable income:",taxable_income)
   print("income tax:",cumulative_tax)
# for age greater than 80
else:
   print("category:'super-senior citizen'")
   tax_percentage = [0,0.2,0.3]
   #tax slabs(the last element of the slab is taxable income because there is no slabs greater than 10l)
   slab=[500000,1000000,taxable_income]
   for i in range(0,len(slab)):
        if taxable_income <= slab[i]:
            if(i==0):
              cumulative_tax = taxable_income * tax_percentage[i]
              i+=1
            else:
              cumulative_tax += (taxable_income-slab[i-1])*tax_percentage[i]
            break
        else:

            if(i==0):
              cumulative_tax += slab[i] * tax_percentage[i]
            else:
               cumulative_tax += (slab[i]-slab[i-1])*tax_percentage[i]
   print("taxable income:",taxable_income)
   print("income tax:",cumulative_tax)


"""
enter your gross salary: 4500000
enter the deductions: 500000
enter your age (age should be greater than 16):30
category: citizen
3000000.0
taxable income: 4000000.0
income tax: 1012500.0
"""
   
        
       
        



   
            
        