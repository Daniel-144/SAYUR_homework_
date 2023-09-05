# Start with the above. The total cost is split equally by bride and groom.
# Bride has saved Rs50000. Determine if the bride has to take a loan or not.
# If loan, how much?
def predefined():
    members_invited = int(input('number of persons invited for the wedding '))
    lunch_per_person = 200
    breakfast_per_person = lunch_per_person / 2
    hall_rent = 200
    lunch_exp = lunch_per_person * members_invited
    breakfast_exp = breakfast_per_person * members_invited
    hall_exp = hall_rent * members_invited
    parking_lot = (10 * hall_exp) / 100
    decoration_cost = (50 * hall_exp) / 100
    print('total lunch expenses : ', lunch_exp)
    print('total breakfast expenses : ', breakfast_exp)
    print('total hall expenses : ', hall_exp)
    print('parking lot expenses : ', parking_lot)
    print('decoration expenses : ', decoration_cost)
    total = lunch_exp + breakfast_exp + hall_exp + parking_lot + decoration_cost
    print('total expenses : ', total)
    return total

print("*****menu*****")
print('1.enter 1 if u want to use the total expenses obtained in the previous program')
print('enter other numbers than 1 if u want to define the total amount spent ')
choice=int(input('enter your choice'))
bride_savings=50000
if choice==1:
    total_expenses=predefined()
    # total expenses split into 2 by bride and groom
    bride_expenses=total_expenses/2
    groom_expenses=total_expenses/2
    print(bride_expenses)

    if bride_expenses > bride_savings:
        print('bride have to take loan ')
        loan_amount = bride_expenses - bride_savings
        print('loan amount would be : ',loan_amount)
    else:
        print('no need for loan')
        remaining_amount=bride_savings-bride_expenses
        print('the remaining amount would be : ',remaining_amount)
else:
    total_expenses=int(input('enter the total expenses : '))
    # total expenses split into 2 by bride and groom
    bride_expenses = total_expenses / 2
    groom_expenses = total_expenses / 2
    if bride_expenses > bride_savings:
        print('bride have to take loan ')
        loan_amount = bride_expenses - bride_savings
        print('loan amount would be : ', loan_amount)
    else:
        print('no need for loan')
        remaining_amount = bride_savings - bride_expenses
        print('the remaining amount would be : ', remaining_amount)

