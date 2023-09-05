######## Problem  2 ###############
#Print multiplication tables from 7 to 16, each number upto 12 rows.
# multipication tables from 7 t to 16 so initializing multiplier range as 16
multiplier_range=16
#each number should be upto 12 rows so multliplicand range is initialized as 12.
multiplicand_range=12
# for loop to print the tables
for multiplier in range(7,multiplier_range+1):
    print(f"table {multiplier}")
    for multiplicand in range(1,multiplicand_range+1):
        print(f"{multiplier} * {multiplicand} = {multiplicand*multiplier}",end=" | ")
    print("")
