"""
1. Write an app for the fruit vendor. Fruit vendor has a list of fruits (apple, Orange, banana etc).
When the customer comes in, vendor asks "What do you want to buy?" .
The customer can say "I want apple", or "Apple" or "three apple" or something like that.
Your program will find out what fruit the customer is asking. 
Your program will also find, if the customer already asked for the quantity of the fruit (one apple or 5 orange etc).
Print the quantity if the customer says the quantity. If not, ask him how much he wants.
Hint : Use string manipulation and lists. https://www.w3schools.com/python/python_ref_string.asp 
You can limit the quantity to single digit number.
"""
import re

# initializing the variables.
fruits=['apple','orange','banana','grapes','mango']
cost=[20,15,7,10,23]
total=0
# order from the user
order=input("what do you want to buy")  
bought=re.findall((r"apple|orange|banana|mango|grape"),order) # regex pattern to find the fruits in the list
pattern2=r'(\d+)\s+(?:apple|orange|grapes|banana|mango)'# pattern to find the quantity of the fruits.
bought_quantity=re.findall(pattern2,order)
# loop to find the fruits and their price
for i,item in enumerate(bought):
    index=fruits.index(item)
    bought_quantity[i]=int(bought_quantity[i])
    print(f"{item} X {bought_quantity[i]}\t-{cost[index]*bought_quantity[i]}RS")
    total+=cost[index]*bought_quantity[i]
print("total:",total)

"""
OP:
apple X 20      -400RS
banana X 10     -70RS
total: 470
"""
    






