num = int(input('enter a number greater than 9 to reverse : '))
rev = 0
# single digit number cannot be reversed. so we use if else statement
if num < 10:
    # as the single digit number cannot be reversed we just display the number which is given as the input.
    print('entered number cannot be reversed and the entered number is : ',num)
else:
    # if it is a double or more than double-digit number the code given in the else part will be executed.
    while num > 0:298
          remain = num % 10
          rev = rev*10+remain
          num = num//10
    print('the reversed version of this given number is : ',rev)

