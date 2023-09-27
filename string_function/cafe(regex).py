# write a program to run a cafe.
# cafe should have a inventory, sales data and profit.

#importing re module
import re

# initaializing variables
menu_card = ["tea", "vadai", "coffee", "biscuit"]
price = [20, 10, 20, 10]
item_quantity = [100, 150, 100, 100]
initial_quantity =[100, 150, 100, 100]
reviews=[]
expenses=0
total=0
cost_price=[10,5,10,5]

#for loop to calculate the expenses
for cost in range (len(item_quantity)):
    expenses += item_quantity[cost]*cost_price[cost]
#while loop to run until the products or empty or no customers visited the shop 
while True:
    # to check if there is no products in the shop.
    if item_quantity != [0,0,0,0]:
        choice=input("did the customers visit the shop(yes/no)?")
        # to check if the customers enter the shop
        if choice.lower() == "yes":
            print(f"{'*'*10}MENU{'*'*10}")
            # for loop for ptinting menu card
            for no,item in enumerate(menu_card) :
                print(f"  {no+1}) {item}\t-{price[no]}rs ")
            order = input("What you need:")
            # Use regular expression to extract numbers
            numbers = re.findall(r'(\d+)\s+(?:coffee|tea|biscuit|vadai)', order)
            items = re.findall(r'\b(coffees?|teas?|vadais?|biscuits?)\b', order)
            bill = 0
            print(f"{'*'*10}bill{'*'*10}")
            for i in range(len(items)):
                index = menu_card.index(items[i])
                num = int(numbers[i])
                if item_quantity[index] == 0 or item_quantity[index] < num:
                    print(f"This Item is not available and we have  {item_quantity[index]} only left")
                else:
                    item_quantity[index] -= num
                    cost = price[index] * num
                    print(f' {menu_card[index]} X {num} \t : {cost}rs')
                    bill += cost
            total+=bill
            print("*"*24)
            print(f'total amount: {bill}')
            # getting revies from the user
            reviews.append(input("enter your review:"))
            print("thank you for the review :)")
        # if no customers enter the shop
        elif choice.lower()=="no":
            print("we are closed")
            print(f"expenses :\t{expenses}")
            print("remaining items")
            # for loop to find the no of products remained after we closed the shop
            for Num,Items in enumerate(menu_card):
              print(f" {Items} initially in the store : {initial_quantity[Num]}  remaining:{item_quantity[Num]}")
            print(f"total money earned:{total}")
            # loop to print the reviews.
            for customer,review in enumerate(reviews):
                print(f"review from customer-{customer+1} is {review}")
            # if elif else statements to print profit or loss 
            if total > expenses:
                print(f"profit:{total-expenses}Rs")
            elif total < expenses:
                print(f"loss:{total-expenses}Rs")
            else:
                print(f"neither profit nor loss:{total-expenses}Rs")
        else:
            print("invalid input")
    else:
        print("we are closed")
        print(f"expenses :\t{expenses}")
        print("remaining items")
        # loop to print the remaining items
        for Num,Items in enumerate(menu_card):
            print(f" {Items} initially in the store : {initial_quantity[Num]}  remaining:{item_quantity[Num]}")
        print(f"total money earned:{total}")
        # loop to print the customer reviews
        for customer,review in enumerate(reviews):
            print(f"review from customer-{customer+1} is {review}")
        # if elif else statement to print profit or loss.
        if total > expenses:
            print(f"profit:{total-expenses}Rs")
        elif total < expenses:
            print(f"loss:{total-expenses}Rs")
        else:
            print(f"neither profit nor loss:{total-expenses}Rs")
        break

"""
OP
did the customers visit the shop(yes/no)?yes
**********MENU**********
  1) tea        -20rs 
  2) vadai      -10rs 
  3) coffee     -20rs 
  4) biscuit    -10rs 
What you need:2 tea and 1 vadai and 20 bisuit
**********bill**********
 tea X 2         : 40rs
 vadai X 1       : 10rs
************************
total amount: 50
enter your review:nice
thank you for the review :)
did the customers visit the shop(yes/no)?yes
**********MENU**********
  1) tea        -20rs
  2) vadai      -10rs
  3) coffee     -20rs
  4) biscuit    -10rs
What you need:20 tea and 30 biscuit 
**********bill**********
 tea X 20        : 400rs
 biscuit X 30    : 300rs
************************
total amount: 700
enter your review:nice
thank you for the review :)
did the customers visit the shop(yes/no)?yes
**********MENU**********
  1) tea        -20rs
  2) vadai      -10rs
  3) coffee     -20rs
  4) biscuit    -10rs
What you need:20 coffee and 30 vadai
**********bill**********
 coffee X 20     : 400rs
 vadai X 30      : 300rs
************************
total amount: 700
enter your review:nice
thank you for the review :)
did the customers visit the shop(yes/no)?no
we are closed
expenses :      3250
remaining items
 tea initially in the store : 100  remaining:78
 vadai initially in the store : 150  remaining:119
 coffee initially in the store : 100  remaining:80
 biscuit initially in the store : 100  remaining:70
total money earned:1450
review from customer-1 is nice
review from customer-2 is nice
review from customer-3 is nice
loss:-1800Rs
"""