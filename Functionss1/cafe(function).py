"""
Problem 6:
You are running a cafe. Write a program (only the functions with input and output) that you need to run the cafe.
"""
import re

# function to calculate the expenses
def calculate_expenses(item_quantity,cost_price):
    #for loop to calculate the expenses
    expenses=0
    for cost in range (len(item_quantity)):
        expenses += item_quantity[cost]*cost_price[cost]
    return(expenses)

# function to print the menu
def print_menu(menu,price):
    print(f"{'*'*10}MENU{'*'*10}")
    # for loop for ptinting menu card
    for no,item in enumerate(menu) :
         print(f"  {no+1}) {item}\t-{price[no]}rs ")

# function to calculate and print the bill
def calculating_bill(menu_card,numbers,items,item_quantity,price):
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
    print("*"*24)
    print(f'total amount: {bill}')
    return(bill)

# function to get reviews from the user.
def getting_reviews():
    review=input("please enter your review:")
    return(review)

# function to print the remaining items in the cafe
def print_remaining_items(expenses,menu_card,initial_quantity,item_quantity,total):
    print("we are closed")
    print(f"expenses :\t{expenses}")
    print("remaining items")
 # for loop to find the no of products remained after we closed the shop
    for Num,Items in enumerate(menu_card):
        print(f" {Items} initially in the store : {initial_quantity[Num]}  remaining:{item_quantity[Num]}")
    print(f"total money earned:{total}")

# function to print the reviews
def print_reviews(reviews):
    for customer,review in enumerate(reviews):
        print(f"review from customer-{customer+1} is {review}")

# function to calculate profit or loss
def calculate_profit_or_loss(expenses,total):
    if total > expenses:
        print(f"profit:{total-expenses}Rs")
    elif total < expenses:
        print(f"loss:{total-expenses}Rs")
    else:
        print(f"neither profit nor loss:{total-expenses}Rs")

# iniatialized variables.
menu_card = ["tea", "vadai", "coffee", "biscuit"]
price = [20, 10, 20, 10]
item_quantity = [100, 150, 100, 100]
initial_quantity =[100, 150, 100, 100]
reviews=[]
total=0
cost_price=[10,5,10,5]
expenses= calculate_expenses(item_quantity,cost_price)

# main loop to run the cafe
while(True):
    # conditional statement to check the items in the cafe
    if item_quantity != [0,0,0,0]:
        choice=input("did the customer visit the store(yes/no):")
        if choice.lower() == "yes":
            print_menu(menu_card,price)
            order = input("What you need:")
            # Use regular expression to extract numbers
            numbers = re.findall(r'(\d+)\s+(?:coffee|tea|biscuit|vadai)', order)
            items = re.findall(r'\b(coffees?|teas?|vadais?|biscuits?)\b', order)
            total+=calculating_bill(menu_card,numbers,items,item_quantity,price)
            reviews.append(getting_reviews())
            print("thank you for the review")
        elif choice.lower()=="no":
            print_remaining_items(expenses,menu_card,initial_quantity,item_quantity,total)
            print_reviews(reviews)
            calculate_profit_or_loss(expenses,total)
            break
        else:
            print("invalid Input")
    else:
        print_remaining_items(expenses,menu_card,initial_quantity,item_quantity,total)
        print_reviews(reviews)
        calculate_profit_or_loss(expenses,total)
        break



