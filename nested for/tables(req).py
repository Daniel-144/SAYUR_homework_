"""
         challenge question
print the tables requested by the user and also Ask the user if they want only the basic or only the advanced or both.
Print what the user is asking.
Also ask the user what number table they want to print
"""
# initialize a list to store the input
tables = []
no_of_tables = int(input('enter the number of tables you want: '))
for index in range(0, no_of_tables):
    # storing the input entered by the user in a list
    tables.append(int(input('enter the table you want : ')))

print("enter 1. if you want to print only easy number")
print("enter 2.if you want to print only advance number")
print("enter 3. if you want to print both ")
choice = int(input('enter your choice: '))

# if the choice is 1 then it will be printing only the easy number
if choice == 1:
    multiplicand_range = 10
    for i in range(0, no_of_tables):
        # basic number 1 to 10 so initialize multiplicand_range as 11
        print('Table {}'.format(tables[i]))
        print('Easy Number')
        for multiplicand in range(1, multiplicand_range+1):
            print('{} * {} = {}'.format(tables[i], multiplicand, tables[i]*multiplicand))
        print('*'*10)
    print('End Of Tables')

# if the choice is 2 then it will be printing the advanced number
elif choice == 2:
    multiplicand_range = 20
    for i in range(0, no_of_tables):
        # advanced numbers 11 to 20 so initializing multiplicand_range as 21
        print('Table {}'.format(tables[i]))
        print('Advanced Number')
        for multiplicand in range(11, multiplicand_range+1):
            print('{} * {} = {}'.format(tables[i], multiplicand, tables[i] * multiplicand))
        print('*' * 10)
    print('end of table')

# else it will be printing the easy and advanced numbers
elif choice == 3:
    multiplicand_range = 20
    for i in range(0, no_of_tables):
        print(f'Tables {tables[i]}')
        print('easy number')
        # classify into simple and advance number by using 2 separate loops to reduce the time complexity
        # loop for simple number
        for multiplicand in range(1, 11):
            product = tables[i] * multiplicand
            print(f"{tables[i]} * {multiplicand} = {product}")
        print('advanced number')
        # loop for advanced numbers
        for multiplicand in range(11, multiplicand_range+1):
            product = tables[i] * multiplicand
            print(f"{tables[i]} * {multiplicand} = {product}")
        print(f"{'*' * 10}")
    print('end of table')

else:
    print("invalid input")
