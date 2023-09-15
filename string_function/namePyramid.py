########## Program 2
#Print your name in a pyramid
#eg RAM
#R
#RA
#RAM

# get the name as the input from the user
name=input("enter your name:")
for i in range(0,len(name)):
    # to iterate the string from the fist after each iterations of while loop.
    j=0
    # loop to print the elements of the array
    while j <= i:
        print(f"{name[j]} ",end="")
        j+=1
    print()

"""                          
enter your name:daniel|enter your name:RAM
d                     |R
d a                   |R A
d a n                 |R A M
d a n i               |
d a n i e             |
d a n i e l           |
"""
