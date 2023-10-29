"""
find the sum of the list using recursion function
"""
# recursive function to get the sum of list
def Sum(list):
    if len(list)==0:
        return 0
    else:
        # recursive part
        return list[0] + Sum(list[1:]) 

# given list
list=[56,23,89,90]
# function call.
print(Sum(list))


