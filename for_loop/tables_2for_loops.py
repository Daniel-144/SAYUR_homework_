"""
2. Print the following using two for loops

1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
2 * 1 = 2
2 * 2 = 4
2 * 3 = 6
2 * 4 = 8
2 * 5 = 10
3 * 1 = 3
3 * 2 = 6
3 * 3 = 9
3 * 4 = 12
3 * 5 =15
"""
# initialize the range of multiplier and multiplicand as per the sample output
multiplier_range = 3
multiplicand_range = 5
""""
the for loop executes the set of code until the given condition is satisfied.
here the multiplicand is incremented until it reaches the end point.
"""
for multiplier in range(1, multiplier_range+1):
    for multiplicand in range(1, multiplicand_range+1):
        print(f'{multiplier} * {multiplicand} = {multiplier * multiplicand}')
