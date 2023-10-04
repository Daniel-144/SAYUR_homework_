"""
Problem 5:
Write a program to sort an array of numbers in ascending order. Use functions.
"""

def sorting_array(array):
    for i in range(len(array)-1):
        for j in range(len(array)-i-1):
            if array[j]>array[j+1]:
                array[j+1],array[j]=array[j],array[j+1]
    return(array)


array=[7,8,3,1,9,0,4,2,3]
sorted_array=sorting_array(array)
print(array)