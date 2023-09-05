""""
4.Print the following
My Tables
Table  10
10 * 1 = 10
10 * 2 = 20
10 * 3 = 30
10 * 4 = 40
10 * 5 = 50
**********
Table  8
8 * 1 = 8
8 * 2 = 16
8 * 3 = 24
8 * 4 = 32
8 * 5 = 40
**********
Table  6
6 * 1 = 6
6 * 2 = 12
6 * 3 = 18
6 * 4 = 24
6 * 5 = 30
**********
Table  4
4 * 1 = 4
4 * 2 = 8
4 * 3 = 12
4 * 4 = 16
4 * 5 = 20
**********
Table  2
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
**********
End of tables
"""
# initialize the range of multiplier and multiplicand as per the sample output
multiplier_range = 10
multiplicand_range=5
""""
the for loop executes the set of code until the given condition is satisfied.
here the multiplicand is incremented until it reaches the end point.
"""
print('My Table')
for multiplier in range(multiplier_range, 0, -2):
    print(f"table {multiplier}")
    for multiplicand in range(1,multiplicand_range+1):
        product = multiplier * multiplicand
        print(f"{multiplier} * {multiplicand} = {product}")
    print(f"{'*' * 10}")
print("End of tables")
