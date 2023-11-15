"""
find the sum of the list using recursion function
"""
# recursive function to get the sum of list
def Sum(list):
    if len(list)==0:
        return 0
    #4th exe- returned 0 to the recursive part.
    else:
        # recursive part
        return list[0] + Sum(list[1:])  
    # 1st exe- 56+sum(23,89,90).
    # 2nd exe- 56+23+sum(89,90).
    # 3rd exe- 56+23+89+sum(90).
    # 4th exe- 56+23+89+90+0.
    

# given list
list=[56,23,89,90]
# function call.
print(Sum(list))


