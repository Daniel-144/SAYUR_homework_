########## Problem 3 ############
#Write a program for a bag shop. Shop has 100 red bags (each Rs 1000) and 200 white bags (each Rs 1500)
#Customers can buy one or more bags at a time.
#The program ends when the sales reached Rs10000 or at least 10 bags are sold. 
#Display total sales and total number of bags sold

#initialize variables
redBags,whiteBags = 100, 200
totalSales,totalBagsSold = 0,9
redBag_cost,whiteBags_cost=1000,1500
total_redbags_bought,total_whitebags_bought=0,0

while (totalSales < 10000 or totalBagsSold < 10) :
    #Ask customer for input
    red_bags_bought=int(input("enter the number of red bags you are going to buy"))
    white_bags_bought=int(input("enter the number of white bags you are going to buy"))
    if redBags >= red_bags_bought and whiteBags >= white_bags_bought:
        totalSales += (red_bags_bought * redBag_cost)+(white_bags_bought * whiteBags_cost)
        redBags -= red_bags_bought
        whiteBags -= white_bags_bought
        total_whitebags_bought += white_bags_bought
        total_redbags_bought += red_bags_bought
        totalBagsSold +=(white_bags_bought+red_bags_bought)
    else:
        if(redBags < red_bags_bought and whiteBags< white_bags_bought):
            print("out of stock come back later!!")
            break
        elif(redBags < red_bags_bought):
            print("red bags are out of stock you can buy white bags")
            totalBagsSold += white_bags_bought
            totalSales += (white_bags_bought * whiteBags_cost)
            whiteBags -= white_bags_bought
            total_whitebags_bought += white_bags_bought
        elif(whiteBags < white_bags_bought):
            print("white bags are out of stock you can buy red bags ")
            totalBagsSold += red_bags_bought
            totalSales += (red_bags_bought * redBag_cost)
            redBags -= red_bags_bought
            total_redbags_bought += red_bags_bought 
totalBagsSold=total_whitebags_bought+total_redbags_bought
print (f" total bags sold:{totalBagsSold}\n total red bags sold:{total_redbags_bought}\n total white bags sold:{total_whitebags_bought}\n total sales:{totalSales}")   