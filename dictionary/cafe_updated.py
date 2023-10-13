"""
Problem 6:
You are running a cafe. Write a program (only the functions with input and output) that you need to run the cafe.
"""
import re

menu={
    "vadai": { "stock": 50, "sellingprice": 15, "costprice":10, "sold":0},
    "coffee": {"stock": 50, "sellingprice": 17, "costprice":12, "sold":0},
    "tea":{ "stock": 50, "sellingprice": 17, "costprice":12, "sold":0},
    "samosa":{"stock": 50, "sellingprice": 20, "costprice":12, "sold":0},
}
order = input("What you need:")
# Use regular expression to extract numbers
numbers = re.findall(r'(\d+)\s+(?:coffee|tea|biscuit|vadai)', order)
items = re.findall(r'\b(coffees?|teas?|vadais?|biscuits?)\b', order)
bill = 0
# loop to calculate the expenses
for items,details in menu.items():
    print(f"{items}\t: {details['sellingprice']}")

