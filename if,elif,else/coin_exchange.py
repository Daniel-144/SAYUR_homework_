# You have three types of coins , values of 1, 3 and 5
# given a number, you need to find minimum coin required
#from typing import Any

money_needed=int(input('enter the amount of money needed :'))
# the total amount is the input given by the user
if money_needed<=0:
    print('invalid input')

else:
 # initializing all the coins as 0
 five_rs = 0
 three = 0
 one_rs = 0
 temp=money_needed
 # used while loop to find the amount of coins needed
 while temp!=0 :
    if temp>=5:
        # to find the amount of five rupee coins needed use floor division and divide the input money by 5
        five_rs=temp//5
        temp2=five_rs * 5
        temp= temp-temp2
    elif temp>=3:
        # to find the amount of three rupee coins needed use floor division and divide the input money by 3
        three = temp // 3
        temp3 = three *3
        temp = temp - temp3
    else:
        # to find the amount of one rupee coins needed
        one_rs=temp
        temp4=one_rs
        temp=temp-temp4
print('no of one rupee coin needed is :',one_rs)
print('no of three rupee coin needed is:',three)
print('no of five rupee coin needed is :',five_rs)


