"""
############## Problem 2 ################
#Use For loop, break and continue as needed.
# You need Rs 1000 to go to movie. you are asking your parents for money. your parents give you a
# some money. Ask your parents for money until you get Rs1000 or a maximum of 5 times.
# Each time they give you some money, you need to print how much money you got so far and print "Thank you.".
# Print "Thank you " only if the money is > Rs 10. If money is less than or = Rs 10, don't add it
# towards the Rs1000 that you need. Use Continue stmt as needed.
# Print how many times you had to ask your parents to get this money.
"""
# initialize the variable
money_given = 0
money_needed = 1000
count = 0
# you have to ask money from your parents 5 times so range is 1,6
for i in range(1, 6):
    # if money got exceeds or equals the money needed then exit the loop
    if money_given < money_needed:
        money = float(input('enter the amount you got from your parents: '))
        count = count + 1
        if money <= 10:
            print("thank you, 'but it will not be useful dont add this ammount to your wallet'")
            continue
        # if money got from parents greater than 10 say thank you and add it to the wallet
        print('thank you')
        money_given += money
    # if money you got from the person
    else:
        break
if money_given >= 1000:
    print(f'got {money_needed}Rs by asking money from parents {count} times. you can go to the movie and you have the balance of RS: {money_given - money_needed}')
else:
    print(f'got money from parents {count} times but you still need {money_needed - money_given} rs to go to the movie')

"""
OP
enter the amount you got from your parents: 100
thank you
enter the amount you got from your parents: 500
thank you
enter the amount you got from your parents: 10
enter the amount you got from your parents: 20
thank you
enter the amount you got from your parents: 500
thank you
got 1000Rs by asking money from parents 5 times. you can go to the movie and you have the balance of RS: 120.0
"""
"""
OP
enter the amount you got from your parents: 10
enter the amount you got from your parents: 9
enter the amount you got from your parents: 600
thank you
enter the amount you got from your parents: 20
thank you
enter the amount you got from your parents: 40
thank you
got money from parents 5 times but you still need 340.0 rs to go to the movie
"""