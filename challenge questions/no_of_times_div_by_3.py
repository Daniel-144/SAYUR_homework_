# Get a number from the user. Divide it by 3 and print the result.
# Divide again by 3 and print the result. Keep dividing until the number is less than 3.
# Print the number of times the number was divided.
num=int(input('enter any number'))
count=0
#stored the number in a temprovary variable
num_1=num
# the loop will be executed if the number is greater than 3.
while num >=3:
    # incremented the count by 1 to know number of times the  number has been divided or the while loop has been executed
    count+=1
    num=num/3
    # used format to produce decimal number with only 2 decimal points.
    #num=format(num,".2f")
    # to know the remaining number after dividing n-th time
    print(f'the the number {num_1} after dividing {count} time is {num}')
# to display the number of times the number is divided by 3.
print(f'the number {num_1} can be divided by 3 {count} times')

"""
OP
enter any number97
the the number 97 after dividing 1 time is 32.333333333333336
the the number 97 after dividing 2 time is 10.777777777777779
the the number 97 after dividing 3 time is 3.592592592592593
the the number 97 after dividing 4 time is 1.197530864197531
the number 97 can be divided by 3 4 times
"""