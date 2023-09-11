# Calculate wedding expenses. Cost for lunch per person is Rs200. Cost for Breakfast per
# person is half of lunch cost. Cost of the hall is Rs 200 per person.
# Decoration is 50% of Hall cost. Parking is 10% of the Hall cost.
# Decide what should be the input and calculate the cost.
members_invited=int(input('number of persons invited for the wedding '))
#initializing variables
lunch_per_person=200
breakfast_per_person=lunch_per_person/2
hall_rent=200
#to claculate lunch expenses
lunch_exp=lunch_per_person * members_invited
# breakfast expenses
breakfast_exp=breakfast_per_person * members_invited
#hall rent
hall_exp=hall_rent * members_invited
# parking lot expenses
parking_lot=(10*hall_exp)/100
# cost for decor
decoration_cost=(50*hall_exp)/100
#0p
print('total lunch expenses : ',lunch_exp)
print('total breakfast expenses : ',breakfast_exp)
print('total hall expenses : ',hall_exp)
print('parkinhg lot expenses : ',parking_lot)
print('decoration expenses : ',decoration_cost)
total=lunch_exp+breakfast_exp+hall_exp+parking_lot+decoration_cost
print('total expenses : ',total)

"""
OP
number of persons invited for the wedding 200
total lunch expenses :  40000
total breakfast expenses :  20000.0
total hall expenses :  40000
parkinhg lot expenses :  4000.0
decoration expenses :  20000.0
total expenses :  124000.0
"""