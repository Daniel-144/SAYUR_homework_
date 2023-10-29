"""
write a python program to calculate the power of the number using recursion
"""
def power(x,n):
    if n==0:
        return 1
    else:
        return (x*power(x,n-1))

power=power(2,0)
print(power)