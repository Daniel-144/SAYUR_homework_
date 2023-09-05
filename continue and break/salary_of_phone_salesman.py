# ############# Problem  3  ####################
# Calculate the monthly salary for the phone salesman
# Base monthly pay Rs10000.
# For every 5 phones sold, Rs 5000 bonus.
# For every phone after the first 5 phones, Rs1100 per phone bonus.
# If the salesman's salary is more than Rs20000 in the previous month and sells 20 or more phones
# this month also, then he gets additional Rs5000.

monthlySalesList = [5, 23, 21, 14, 23, 12, 4, 12, 22, 22, 34, 12]  # Sample number of phones sold in each month in a year

basic_pay = 10000
bonus_5_phones = 5000
bonus_after_5_phones = 1100
bonus_for_consistency = 5000
previousMonthSalary = 10000
# for calculating the monthly salary of a person
for month, phoneCount in enumerate(monthlySalesList, 1):
    # to check if the person has sold less than 5 phones
    if phoneCount >= 5:
        salary = basic_pay + (phoneCount-5)*bonus_after_5_phones + bonus_5_phones
    else:
        salary = basic_pay
    current_salary = salary
    print(f"the monthly salary for month-{month} before addition of bonus is {basic_pay}")
    # to check if the person has sold  less than 20 phones
    if phoneCount < 20:
        # store the current salary of the person as previous month salary for next iteration
        previousMonthSalary = current_salary
        # if  phone count is less than
        print(f"the monthly salary for month-{month} after addition of bonus is {current_salary}\n")
        continue
    else:
        if previousMonthSalary > 20000:
            current_salary += bonus_for_consistency
            print(f"the monthly salary for month-{month} after the addition of bonus is {current_salary}\n")
            previousMonthSalary = current_salary
        else:
            # for next iteration we store the current salary to the previous salary
            print(f"the monthly salary for month-{month} after addition of bonus is {current_salary}\n")
            previousMonthSalary = current_salary
            continue

    """
    OP
the monthly salary for month-1 before addition of bonus is 10000
the monthly salary for month-1 after addition of bonus is 15000

the monthly salary for month-2 before addition of bonus is 10000
the monthly salary for month-2 after addition of bonus is 34800

the monthly salary for month-3 before addition of bonus is 10000
the monthly salary for month-3 after the addition of bonus is 37600

the monthly salary for month-4 before addition of bonus is 10000
the monthly salary for month-4 after addition of bonus is 24900

the monthly salary for month-5 before addition of bonus is 10000
the monthly salary for month-5 after the addition of bonus is 39800

the monthly salary for month-6 before addition of bonus is 10000
the monthly salary for month-6 after addition of bonus is 22700

the monthly salary for month-7 before addition of bonus is 10000
the monthly salary for month-7 after addition of bonus is 10000

the monthly salary for month-8 before addition of bonus is 10000
the monthly salary for month-8 after addition of bonus is 22700

the monthly salary for month-9 before addition of bonus is 10000
the monthly salary for month-9 after the addition of bonus is 38700

the monthly salary for month-10 before addition of bonus is 10000
the monthly salary for month-10 after the addition of bonus is 38700

the monthly salary for month-11 before addition of bonus is 10000
the monthly salary for month-11 after the addition of bonus is 51900

the monthly salary for month-12 before addition of bonus is 10000
the monthly salary for month-12 after addition of bonus is 22700
"""