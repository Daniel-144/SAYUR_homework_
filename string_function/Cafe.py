# write a program to run a cafe.
# cafe should have a inventory, sales data and profit.

# intializing lists to store the data
products=[]
cost=[]
supplies=[]
sellingPrice=[]
sold=[]
tempStock=[]
orderedByCustomer=[]

#getting the number of items to be given in the menu as input from the user
NoItems=int(input("enter the number of items to be given in the menu"))
# using for loop to get the item and its details.(eg:stock,cost price and selling price)
for i in range(NoItems):
    item=input("enter the product to be given in the menu:")
    costOfMaking=float(input("enter the cost price of the item:"))
    stock=int(input(f"enter the quantity of {item} you have in your cafe:"))
    selling_price=float(input("enter the selling price:"))
    products.append(item)
    cost.append(costOfMaking)
    supplies.append(stock)
    sellingPrice.append(selling_price)
    sold.append(0)
    tempStock.append(0)
    orderedByCustomer.append(0)
# initializing expense and total sales
expense=0
totalSales=0
# for loop for caalculating expenses
for i in range(len(products)):
    expense+=supplies[i]*cost[i]
print(expense)
noCustomer=0
# list to store review from the customer
reviews=[]
# while loop to stop when we have no customers or we are out of stock
while(True):
    customer_visited=input("does the customer visited the store(y/n): ")
    if customer_visited.lower() =='y'and supplies > tempStock:
        noCustomer+=1
        bill=0
        # ordered by the customers increasses so we use for loop to bring it back to 0 after each iteration
        for orders in range(0,len(products)):
            orderedByCustomer[orders]=0

        #for loop for menu
        print(f"{'*'*10}menu{'*'*10}")
        for menu in range(len(products)):
            print(f"enter {menu} to order {products[menu]}",end="")
            print(f" RS{sellingPrice[menu]}")
        # loop for getting orders and calculation of bill
        while(True):
            choice=input("do u want to order (yes/no):")
            if choice.lower()=="yes":
                orderChoice=int(input("enter your choice of order based on the menu: "))
                if orderChoice<len(products):
                    order=int(input(f"enter the quantity of {products[orderChoice]} you want:"))
                    if supplies[orderChoice]<order:
                        print("sorry we are out of stock")
                    else:
                        orderedByCustomer[orderChoice]+=order
                        bill+=sellingPrice[orderChoice]*order
                        sold[orderChoice]+=order
                        supplies[orderChoice]-=order  
                else:
                    print("no such product exist")
            else:
             # loop for printing bill and getting feedback
             for product in range(len(products)):
                 print(f"{products[product]}\t",end=" ")
                 print(f"quantity {orderedByCustomer[product]}=Rs {sellingPrice[product]*orderedByCustomer[product]}")
             print("*"*30)
             print("\tbill=",bill)
             totalSales+=bill
             feedback=input("enter your feedback:")
             # the feedback of the customers will be stored in a list called review
             reviews.append(feedback)
             break  
    # else statement to calculate the today's sale and to print the customers feedback
    else:
        # tempstocks is a array of 0's compare our supplies with tempstock to check if all supplies are zero
        if supplies == tempStock:
            print("everything sold out")
        print("we're closed")
        print("expenses:",expense)
        print("total number of customers visited:",noCustomer)
        print("\t today's sales")
        # loop for calculating the amount of product sold and remaining.
        for itemsSold in range(len(products)):
            print(f"total number of {products[itemsSold] } is {sold[itemsSold]} remaining:{supplies[itemsSold]}")
        print(f"today's total sales={totalSales}")
        # if elif else statements for calculating profit or loss
        if totalSales-expense > 0:
            print(f"we got a profit of amount :{totalSales-expense}")
        elif totalSales-expense < 0:
            print("loss:",totalSales-expense)
        else:
            print("no profit no loss")
        for review in range(len(reviews)):
            print(f"review from customer {review+1} is :{reviews[review]}")
        break
    
"""
OP
enter the number of items to be given in the menu:4
enter the product to be given in the menu:tea
enter the cost price of the item:6
enter the quantity of tea you have in your cafe:100
enter the selling price:12
enter the product to be given in the menu:vadai
enter the cost price of the item:5
enter the quantity of vadai you have in your cafe:100
enter the selling price:10
enter the product to be given in the menu:coffee
enter the cost price of the item:5
enter the quantity of coffee you have in your cafe:100
enter the selling price:10
enter the product to be given in the menu:samosa
enter the cost price of the item:6
enter the quantity of samosa you have in your cafe:100
enter the selling price:12
2200.0
does the customer visited the store(y/n): y
**********menu**********
enter 0 to order tea RS12.0
enter 1 to order vadai RS10.0
enter 2 to order coffee RS10.0
enter 3 to order samosa RS12.0
do u want to order (yes/no):0
tea      quantity 0=Rs 0.0
vadai    quantity 0=Rs 0.0
coffee   quantity 0=Rs 0.0
samosa   quantity 0=Rs 0.0
******************************
        bill= 0
enter your feedback:not intrested in the menu
does the customer visited the store(y/n): y
**********menu**********
enter 0 to order tea RS12.0
enter 1 to order vadai RS10.0
enter 2 to order coffee RS10.0
enter 3 to order samosa RS12.0
do u want to order (yes/no):yes
enter your choice of order based on the menu: 1
enter the quantity of vadai you want:5
do u want to order (yes/no):yes
enter your choice of order based on the menu: 3
enter the quantity of samosa you want:10
do u want to order (yes/no):yes
enter your choice of order based on the menu: 0
enter the quantity of tea you want:10
do u want to order (yes/no):yes
enter your choice of order based on the menu: 2
enter the quantity of coffee you want:5
do u want to order (yes/no):no
tea      quantity 10=Rs 120.0
vadai    quantity 5=Rs 50.0
coffee   quantity 5=Rs 50.0
samosa   quantity 10=Rs 120.0
******************************
        bill= 340.0
enter your feedback:good
does the customer visited the store(y/n): y
**********menu**********
enter 0 to order tea RS12.0
enter 1 to order vadai RS10.0
enter 2 to order coffee RS10.0
enter 3 to order samosa RS12.0
do u want to order (yes/no):yes
enter your choice of order based on the menu: 0
enter the quantity of tea you want:15
do u want to order (yes/no):yes
enter your choice of order based on the menu: 1
enter the quantity of vadai you want:15
do u want to order (yes/no):yes
enter your choice of order based on the menu: 2
enter the quantity of coffee you want:20
do u want to order (yes/no):yes
enter your choice of order based on the menu: 3
enter the quantity of samosa you want:10
do u want to order (yes/no):no
tea      quantity 15=Rs 180.0
vadai    quantity 15=Rs 150.0
coffee   quantity 20=Rs 200.0
samosa   quantity 10=Rs 120.0
******************************
        bill= 650.0
enter your feedback:better than expected
does the customer visited the store(y/n): y
**********menu**********
enter 0 to order tea RS12.0
enter 1 to order vadai RS10.0
enter 2 to order coffee RS10.0
enter 3 to order samosa RS12.0
do u want to order (yes/no):0
tea      quantity 0=Rs 0.0
vadai    quantity 0=Rs 0.0
coffee   quantity 0=Rs 0.0
samosa   quantity 0=Rs 0.0
******************************
        bill= 0
enter your feedback:only 4 items in the menu
does the customer visited the store(y/n): y
**********menu**********
enter 0 to order tea RS12.0
enter 1 to order vadai RS10.0
enter 2 to order coffee RS10.0
enter 3 to order samosa RS12.0
do u want to order (yes/no):yes
enter your choice of order based on the menu: 1
enter the quantity of vadai you want:30
do u want to order (yes/no):yes
enter your choice of order based on the menu: 3
enter the quantity of samosa you want:30
do u want to order (yes/no):yes
enter your choice of order based on the menu: 0
enter the quantity of tea you want:20
do u want to order (yes/no):yes
enter your choice of order based on the menu: 2
enter the quantity of coffee you want:20
do u want to order (yes/no):no
tea      quantity 20=Rs 240.0
vadai    quantity 30=Rs 300.0
coffee   quantity 20=Rs 200.0
samosa   quantity 30=Rs 360.0
******************************
        bill= 1100.0
enter your feedback:nice
does the customer visited the store(y/n): y
**********menu**********
enter 0 to order tea RS12.0
enter 1 to order vadai RS10.0
enter 2 to order coffee RS10.0
enter 3 to order samosa RS12.0
do u want to order (yes/no):yes
enter your choice of order based on the menu: 0
enter the quantity of tea you want:20
do u want to order (yes/no):no
tea      quantity 20=Rs 240.0
vadai    quantity 0=Rs 0.0
coffee   quantity 0=Rs 0.0
samosa   quantity 0=Rs 0.0
******************************
        bill= 240.0
enter your feedback:good
does the customer visited the store(y/n): n
we're closed
expenses: 2200.0
total number of customers visited: 6
         today's sales
total number of tea  sold is 65 remaining:35
total number of vadai sold is 50 remaining:50
total number of coffee sold is 45 remaining:55
total number of samosa sold is 50 remaining:50
today's total sales=2330.0
we got a profit of amount :130.0
review from customer 1 is :not intrested in the menu
review from customer 2 is :good
review from customer 3 is :better than expected
review from customer 4 is :only 4 items in the menu
review from customer 5 is :nice
review from customer 6 is :good
"""
        
        




