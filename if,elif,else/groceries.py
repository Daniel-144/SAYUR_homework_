#Program to find out how many Kg of onion or tomato we can buy. One Kg of Onion is 20rs, Tomato is 10.5rs.  Input is the budget.
#7.1 Same as above, but the price of Onion is different based on the city. Chennai - Rs30, Trichy Rs27, Madurai Rs 34. Input is budget and city.
# 7.2 Same as above, but add 3% of the budget for petrol expenses.
def product_bought(amt,tomato,opt):
    # for chennai
    if opt==1:
        onion=30
        bought_tomato =amt/tomato
        onion_bought=amt/onion
        onion_bought = format(onion_bought, ".2f")
        bought_tomato = format(bought_tomato, ".2f")
        return (f'you can buy {bought_tomato} kg of tomato or you can buy {onion_bought} kg of onion ')
    # for trichy
    elif opt==3:
        onion=27
        bought_tomato =amt/tomato
        onion_bought=amt/onion
        onion_bought = format(onion_bought, ".2f")
        bought_tomato = format(bought_tomato, ".2f")
        return (f'you can buy {bought_tomato} kg of tomato or you can buy {onion_bought} kg of onion ')
    # for madurai
    elif opt==2:
        onion=34
        bought_tomato =amt/tomato
        onion_bought=amt/onion
        onion_bought = format(onion_bought, ".2f")
        bought_tomato = format(bought_tomato, ".2f")
        return (f'you can buy {bought_tomato} kg of tomato or you can buy {onion_bought} kg of onion ')
    # elsewhere
    else:
        onion=20
        bought_tomato =amt/tomato
        onion_bought=amt/onion
        onion_bought = format(onion_bought, ".2f")
        bought_tomato = format(bought_tomato, ".2f")
        return (f'you can buy {bought_tomato} kg of tomato or you can buy {onion_bought} kg of onion ')


budget= int(input('enter the amount of money you have'))
# enter the city located near you this program is only applicable for chennai, Trichy and ,madurai.
tomato=10.5
travel_expenses=(3*budget)/100
print(travel_expenses)
shopping_amount= budget-travel_expenses
print(shopping_amount)
if shopping_amount < tomato:
    print('sorry u cannot buy anything with the amount you have')
else:
    print('*****MENU*****')
    print('1.chennai')
    print('2.madurai')
    print('3.trichy')
    print('other city=any number if its not in the list')
    option=int(input('enter the option: '))
    buyable_products= product_bought(shopping_amount,tomato,option)
    print(buyable_products)

"""
OP
enter the amount of money you have1000
30.0
970.0
*****MENU*****
1.chennai
2.madurai
3.trichy
other city=any number if its not in the list
enter the option: 2
you can buy 92.38 kg of tomato or you can buy 28.53 kg of onion 
"""