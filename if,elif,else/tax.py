# to calculate the the income tax for an individual based on each tax slab.
"""""
income tax calculation based on the old tax regime.
according to old regime everyone are categorized based on their ages.
*age<60 - citizen category.
*age>60 and age<=80 - senior citizen category.
*age>80 -super senior citizen category.
tax based on category
      citizen                              |      senior citizen                       |   super senior citizen                      |
taxable income<=300000- tax=0              |taxable income<=300000- tax=0              |taxable income<=500000- tax=0                |
taxable income: 300000 to 500000 - tax=5%  |taxable income: 300000 to 500000 - tax=5%  |taxable income: 500000 to 10000000 -tax=20%  |
taxable income: 500000 to 1000000- tax=20% |taxable income: 500000 to 10000000 -tax=20%|taxable income>1000000                       |
taxable income> 1000000 - tax=30%          |taxable income>1000000                     |
"""
import array as arr

gross_salary = float(input("enter your gross salary: "))
deductions = float(input('enter the deductions: '))
taxable_income = gross_salary-deductions
age = int(input("enter your age (age should be greater than 16):"))
temp = taxable_income
cumulative_tax = 0
tax_percentage = [0.05, 0.1, 0.15, 0.2, 0.3]
# use if else to get rid of runtime errors
if (gross_salary<0 or taxable_income<0 or gross_salary<deductions or age<16 or deductions<0) :
    print("invalid input")
    #categorize them into citizen-if their age is below 60,senior-citizen if their age is below  80 and above 59,super senior citizen if above 80
    if age < 60:
        slab = [300000, 500000, 1000000, 1500000]
        print('age: ',age)
        print(f'gross income: {gross_salary}\n deductions: {deductions}\n taxable income: {taxable_income}')
        # if the amount is below 300000 they don't need to pay tax
        if(taxable_income <= slab[0]):
            tax=0
            print('tax : ',tax)
        #if the taxable income is below amount 500000 and above 300000 they have to pay 5% as tax
        elif(taxable_income <= slab[1]):
            temp=temp-slab[0]
            tax=temp*tax_percentage[0]
            print('tax : ',tax)
        #if the taxable income is below 1000000 and above 500000 they have to pay 20%
        elif(taxable_income <= slab[3]):
            temp=temp-slab[2]
            tax=(slab[1]-slab[0])*tax_percentage[0] + (slab[2]-slab[1])*tax_percentage[1]+(temp * tax_percentage[2])
            print('tax : ',tax)
        #if the taxable income is below amount 1500000 they have to pay 20% and 90000rs as tax
        elif(taxable_income <= slab[4]):
            temp=temp-slab[3]
            tax=(slab[1]-slab[0])*tax_percentage[0] +(slab[2]-slab[1])*tax_percentage[1] + (slab[3]-slab[2])*tax_percentage[2]+(temp * tax_percentage[3])
            print('tax : ',tax)
        #if the taxable income is above amount 1500000 they have to pay 30% and 150000rs as tax
        else:
            temp=temp-slab[4]
            tax=(slab[1]-slab[0])*tax_percentage[0] +(slab[2]-slab[1])*tax_percentage[1] +(slab[3]-slab[2])*tax_percentage[2] +(slab[4]-slab[3])*tax_percentage[3]+(temp *tax_percentage[3])
            print('tax : ',tax)
    elif(age>=60 and age<=80):
        slab = [300000,500000,1000000,1500000]
        print('category : senior citizen ')
        print('age: ',age)
        print(f'gross income: {gross_salary}\n deductions: {deductions}\n taxable income: {taxable_income}')
        # if the amount is below 300000 they don't need to pay tax
        if taxable_income<=slab[0]:
            tax=0
            print('tax : ',tax)
        # if the taxable income is below amount 500000 they have to pay 5% as tax and 4% as cess
        elif taxable_income>slab[0] and taxable_income<=slab[1]:
            temp=taxable_income-slab[0]
            tax=temp*tax_percentage[0]
            cess=tax*0.04
            print(f'tax :{tax}\n cess:{cess}' )
        # if the taxable income is below amount 1000000 they have to pay 20%and 10000 as tax and 4% as cess
        elif(taxable_income>slab[1] and taxable_income<=slab[2]):
            temp=taxable_income-slab[1]
            tax=(slab[1]-slab[0])*tax_percentage[0]+(temp*tax_percentage[0.3])
            cess=tax*0.04
            print(f'tax :{tax}\n cess:{cess}' )
            # if the taxable income is greater than amount 1000000 they have to pay 20%and 10000 as tax and 4% as cess
        else:
            temp=taxable_income-slab[2]
            tax=(slab[1]-slab[0])*0.05+(slab[1]-slab[2])*0.2+(temp*0.3)
            cess=tax*0.04
            print(f'tax :{tax}\n cess:{cess}' )
        # for super senior citizens
    else:
        slab = [500000,1000000]
        print('category : super-senior citizen')
        print('age: ',age)
        print(f'gross income: {gross_salary}\n deductions: {deductions}\n taxable income: {taxable_income}')
        # if the amount is below 500000 they don't need to pay tax
        if taxable_income<=slab[0]:
            tax=0
            cess=0
            print('tax : ',tax)
         # if the taxable income is below amount 1000000 they have to pay 20%and 10000 as tax and 4% as cess.
        elif taxable_income>slab[0] and taxable_income<=slab[1]:
            temp = taxable_income-slab[0]
            tax = temp*0.2
            cess=tax*0.04
            print(f'tax :{tax}\n cess:{cess}' )
        # if the taxable income is above amount 1000000 they have to pay 30%and 10000 as tax and 4% as cess
        else:
            temp = taxable_income-slab[1]
            tax = (slab[1]-slab[0])*0.2+(temp*0.3)
            cess = tax*0.04
            print(f'tax :{tax}\n cess:{cess}' )


            
        