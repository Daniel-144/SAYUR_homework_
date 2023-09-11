# to calculate the  income tax for an individual based on each tax slab.

gross_salary = int(input("enter your gross salary: "))
deductions = int(input('enter the deductions: '))
taxable_income = gross_salary-deductions
age=int(input("enter your age: "))
temp=taxable_income
tax=0
min_amount=300000
slab2=600000
slab3=900000
slab4=1200000
slab5=1500000
# use if else to get rid of runtime errors
if gross_salary < 0 or taxable_income < 0 or gross_salary<deductions or age < 1:
    print("invalid input")
else:
    # categorize them into citizen-if they are below 60
    # senior citizen-if they are below 80
    # super senior citizen if above 80
    if age < 60:
        print('category : citizen')
        print('age: ',age)
        print(f'gross income: {gross_salary}\n deductions: {deductions}\n taxable income: {taxable_income}')
        # if the amount is below 300000 they don't need to pay tax
        if taxable_income <= min_amount:
            tax=0
            print('tax : ',tax)
        # if the taxable income is below amount 600000 they have to pay 5% as tax
        elif taxable_income <= slab2:
            temp=temp-min_amount
            tax=temp*0.05
            print('tax : ',tax)
        # if the taxable income is below amount 900000 they have to pay 10% and 15000rs as tax
        elif taxable_income <= slab3:
            temp=temp-slab2
            tax=15000+(temp * 0.1)
            print('tax : ',tax)
        # if the taxable income is below amount 1200000 they have to pay 15% and 45000rs as tax
        elif taxable_income <= slab4:
            temp=temp-slab3
            tax=45000+(temp * 0.15)
            print('tax : ', tax)
        # if the taxable income is below amount 1500000 they have to pay 20% and 90000rs as tax
        elif taxable_income <= slab5:
            temp=temp-slab4
            tax=90000+(temp * 0.2)
            print('tax : ',tax)
        # if the taxable income is above amount 1500000 they have to pay 30% and 150000rs as tax
        else:
            temp=temp-slab5
            tax=150000+(temp *0.3)
            print('tax : ',tax)
    elif age >= 60 and age <= 80:
        minimum_amount = 300000
        slab_2 = 500000
        slab_3 = 1000000
        print('category : senior citizen ')
        print('age: ', age)
        print(f'gross income: {gross_salary}\n deductions: {deductions}\n taxable income: {taxable_income}')
        # if the amount is below 300000 they don't need to pay tax
        if taxable_income <= minimum_amount:
            tax=0
            print('tax : ',tax)
        # if the taxable income is below amount 500000 they have to pay 5% as tax and 4% as cess
        elif taxable_income>minimum_amount and taxable_income<=slab_2:
            temp=taxable_income-minimum_amount
            tax=temp*0.05
            cess=tax*0.04
            print(f'tax :{tax}\n cess:{cess}' )
        #if the taxable income is below amount 1000000 they have to pay 20%and 10000 as tax and 4% as cess
        elif(taxable_income>slab_2 and taxable_income<=slab_3):
            temp=taxable_income-slab_2
            tax=10000+(temp*0.2)
            cess=tax*0.04
            print(f'tax :{tax}\n cess:{cess}' )
            #if the taxable income is above amount 1100000 they have to pay 20%and 10000 as tax and 4% as cess
        else:
            temp=taxable_income-slab3
            tax=110000+(temp*0.3)
            cess=tax*0.04
            print(f'tax :{tax}\n cess:{cess}' )
        #for super senior citizens
    else:
        print('category : super-senior citizen')
        print('age: ',age)
        print(f'gross income: {gross_salary}\n deductions: {deductions}\n taxable income: {taxable_income}')
        minimum_amount=500000
        slab_2=1000000
        cess=0
        # if the amount is below 500000 they don't need to pay tax
        if(taxable_income<=minimum_amount):
            tax=0
            print('tax : ',tax)
         #if the taxable income is below amount 1000000 they have to pay 20%and 10000 as tax and 4% as cess
        elif(taxable_income>minimum_amount and taxable_income<=slab_2):
            temp=taxable_income-minimum_amount
            tax=temp*0.2
            cess=tax*0.04
            print(f'tax :{tax}\n cess:{cess}' )
        #if the taxable income is above amount 1000000 they have to pay 30%and 10000 as tax and 4% as cess
        else:
            temp=taxable_income-slab_2
            tax=100000+(temp*0.3)
            cess=tax*0.04
            print(f'tax :{tax}\n cess:{cess}' )

"""
OP
enter your gross salary: 4500000
enter the deductions: 500000
enter your age: 45
category : citizen
age:  45
gross income: 4500000
 deductions: 500000
 taxable income: 4000000
tax :  900000.0
"""
