######## Problem 2 ###############
# Computer will guess a random number. 
# user has to guess that number. for each guess, print 'High' or 'Low'
# eg - computer number - 189
# user guess 56 - print low
# user guess 678 - print high
# Get user input and print 'high' or 'low' until the user guesses the number correctly 
# https://www.w3schools.com/python/ref_random_randint.asp - read this to learn how to create a random number

# to generate random integer we imort random
import random
# storing the random number within the range of 3 to 9 in computerNo
computerNo = random.randint(3, 9)
attempt = 0
# use while loop to perform the code until the user predicts the random integer
while(True):
    userNo = int (input("enter a number between 3 to 9:"))
    attempt +=1
    # if he predicts the correct number it will break out of the loop
    if ( userNo == computerNo):
        print("high")
        break
    else:
        print("LOW")
print("number of attempt:",attempt)
print("correct guess the random integer predicted by the computer is:",userNo)
    
    