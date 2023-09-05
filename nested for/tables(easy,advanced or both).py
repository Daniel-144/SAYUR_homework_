"""
6. Same as the above. Ask the user if they want only the basic or only the advanced or both.
Print what the user is asking.
Also ask the user what number table they want to print
"""
print("enter 1. if you want to print only easy number\nenter 2.if you want to print only advance number\nenter any if you want to print both ")
choice = int(input("enter your choice"))
multiplier = int(input('enter the value of the multiplier'))
if choice == 1:
    multiplicand_range = 10
    print(f'Table {multiplier}')
    print('Easy Number')
    for i in range(1,multiplicand_range+1):
        print(f'{multiplier} * {i} = {multiplier*i}')
    print('*'*10)

elif choice==2:
    multiplicand_range = 20
    print(f'Table {multiplier}')
    print('Advanced NUmber')
    for i in range(11,multiplicand_range):
        print(f'{multiplier} * {i} = {multiplier*i}')
    print('*'*10)
else:
    multiplicand_range=20
    print(f'Table {multiplier}')
    print('Easy Number')
    for i in range(1,11):
        print(f'{multiplier} * {i} = {multiplier*i}')
    print('Advanced Number')
    for i in range(11, multiplicand_range + 1):
        print(f'{multiplier} * {i} = {multiplier * i}')
    print('*' * 10)
print('end of table')








