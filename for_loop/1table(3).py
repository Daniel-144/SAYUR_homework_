"""
1. Print the following using for loop
1 * 1 = 1
1 * 2 = 2
1 * 3 = 3
1 * 4 = 4
1 * 5 = 5
"""
multiplier = 1
# the end_point is the factor which decides when the program ends.
end_point = 5
""""
the for loop executes the set of code until the given condition is satisfied.
here the multiplicand is incremented until it reaches the end point.
"""
for multiplicand in range(1,end_point+1):
    print(f'{multiplier} * {multiplicand} = {multiplier*multiplicand}')