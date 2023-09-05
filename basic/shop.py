your_money =float(input('enter the amount you have : '))
cost_of_vadai = 30.00
cost_of_soda = 20.00
cost_of_sandwich =100.00
print('*****menu*****')
print('the cost of vadai is : 30')
print('the cost of soda is : 20')
print('the cost of sandwich is : 100')
if your_money < cost_of_soda:
    print('you cannot buy anything with the money you have')
else :
    order_vadai = int(input('enter the number of vadai you want : '))
    order_soda = int(input('enter the number of soda you want : '))
    order_sandwich = int(input('enter the number of sandwich you want : '))
    total = (order_vadai * cost_of_vadai)+(order_soda * cost_of_soda)+(order_sandwich * cost_of_sandwich)
    if total>your_money:
        print('the cost of the bill is greater than the money you have.')
    else:
        balance= your_money-total
        print("the balance money is : ",balance)

