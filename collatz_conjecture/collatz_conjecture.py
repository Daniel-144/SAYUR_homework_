"""
write a program for collatz_conjecture.
# Collatz_conjecture means - start with input number.
# for even number , divide by 2(n/2)
# for odd number - 3n+1
# apply the above for the result number until the answer number is 1
"""
number = int(input("enter the input number:"))
count=0 # initialized counter to count the number of iteration
while(number != 1):
    count+=1 # to count the number of iteration
    if ( number % 2 == 0): 
        number = number//2  # for even number , divide by 2(n/2)
    else:
        number=(3*number)+1
print(f"number became {number} after {count} iterations")