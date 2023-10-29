"""
factorial of a number using recursion function.
"""
def fact(n):
    if (n==1 or n==0):
        return 1
    
    else:
        res= n*fact(n-1)
        return(res)
    
n=5
print(fact(n))