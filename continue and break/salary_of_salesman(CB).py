############## Problem  3  #################### 
#Calculate the monthly salary for the phone salesman
#Base monthly pay Rs10000. 
#For every 5 phones sold, Rs 5000 bonus.
#For every phone aftr the first 5 phones, Rs1100 per phone bonus.
#If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
# this month also, then he gets additional Rs5000.
# if his cumulative bonus is greater than 1lakh his base pay should be increased by 5%


monthlySalesList = [5,23,21,14,23,12,4,12,22,22,34,12]  # Sample number of phones sold in each month in a year
bonus=0
base_pay=10000
bonus_for_5_phones=5000
bonus_after_5_phones=1100
consistency_bonus=5000
previousMonthSalary=base_pay
for month, phoneCount in enumerate(monthlySalesList,1):
    #calculate the Salary using If stmts
    if phoneCount >= 5:
        bonus += bonus_for_5_phones + (phoneCount - 5) * bonus_after_5_phones
        currentMonthSalary = base_pay + bonus_for_5_phones + (phoneCount - 5) * bonus_after_5_phones
    else:
        currentMonthSalary=base_pay
    print(f"salary of month {month} before the additional bonus is : {base_pay}")
    print(f"cumulative bonus: ",bonus)
    #check for condition #If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones 
    # this month also, then he gets additional Rs5000.
    #to check if his phone count is lesser than or equal to 20 and his cumulative bonus is lesser than 1lakh
    if(phoneCount < 20 and bonus <= 100000 ):
        print(f"salary of month {month} after additional bonus is : {currentMonthSalary}\n")
        previousMonthSalary = currentMonthSalary 
        continue
        #no need to calculate anything because <20 phones sold and cumulative bonus is also lesser than or equal to 1lakh
    else:
        if(previousMonthSalary >= 20000 and phoneCount >= 20):
            currentMonthSalary= currentMonthSalary + consistency_bonus
            bonus+=consistency_bonus
            print("cumulative bonus after the addition of consistancy bonus is : ",bonus)
        else:
            previousMonthSalary=currentMonthSalary
        if(bonus > 100000):
            #if his cummularive bonus is greater than 1 lakh then his base pay increases by 5%
            base_pay += base_pay*0.05 
        print(f"salary of month {month} after additional bonus {currentMonthSalary}\n")
        previousMonthSalary = currentMonthSalary # to use this salary to the next iteration so we use to save current salary to the variable called previousmonthsalary
