"""
Problem 6:
You are running a cafe. Write a program (only the functions with input and output) that you need to run the cafe.
"""
import re

menu={
    "vadai": { "stock": 100, "sellingprice": 15, "costprice":10, "sold":0},
    "coffee": {"stock": 100, "sellingprice": 17, "costprice":12, "sold":0},
    "tea":{ "stock": 100, "sellingprice": 17, "costprice":12, "sold":0},
    "samosa":{"stock": 100, "sellingprice": 20, "costprice":12, "sold":0},
}
expenses = 0
earned=0
# loop to calculate the expenses
for customers in range(1,11):
    bill=0
    for products,details in menu.items():
        print(f"{products}\t: {details['sellingprice']} RS")
        expenses+= details["costprice"]
    order = input("What you need:")
    # Use regular expression to extract numbers
    quantity = re.findall(r'(\d+)\s+(?:coffee|tea|samosa|vadai)', order)
    items = re.findall(r'\b(coffees?|teas?|vadais?|samosas?)\b', order)
    for item in range(len(items)):
        if int(quantity[item])<menu[items[item]]["stock"]:
            menu[items[item]]["stock"] -= int(quantity[item])
            menu[items[item]]["sold"] += int(quantity[item])
        else:
            print(f"only {menu[items[item]]['stock']} {items[item]} left")
    print("\tBILL\t")
    for product in range(len(items)):
        print(f"{items[product]} X {quantity[product]}\t:{int(quantity[product])*menu[items[product]]['sellingprice']}")
        bill += int(quantity[product]) * menu[items[product]]['sellingprice']
    print(f"{'*'*10}")
    print(f"Total:{bill}\n")

for products,details in menu.items():
    earned += details["sellingprice"] * ["sold"]
    
if earned > expenses:
    print(f"profit:{earned-expenses}")
elif earned < expenses:
    print(f"loss:{earned-expenses}")
else:
    print("neither profit nor loss.")
    



