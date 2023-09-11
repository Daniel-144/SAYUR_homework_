#average distance between madurai to chennai is 456km
#spider-man plans to go to chennai from madurai
#assume he has 2 energy and he gains 2 energy points by drinking coffee
distance=456
distance_travelled=0
coffee_consumed=0
selfies_posted=0
bus=0
energy=2
temp=distance
#he needs a tall building to jump over
#and the distance between the buildings should be 1km.
while distance_travelled<distance:
    print("* if there is any tall buildings press '1' \n *else press 'any other number'")
    choice=int(input('is there any tall building? '))
    if choice==1:
        if energy>0:
             distance_travelled+=1
             energy-=1
             selfies_posted+=1
             print('distacne travelled by him:',distance_travelled)
        #tall building found we have to check if he has sufficient energy.
        else:
             coffee_consumed+=1
             energy+=2
             distance_travelled+=1
             energy-=1
             selfies_posted+=1
             print('distance travelled by him:',distance_travelled)
    # no tall buildings found.
    else:
        print('no tall buildings found he has to travell in a bus')
        distance_travelled+=10
        bus+=1
        print('distance travelled by him:',distance_travelled)
        difference = temp - distance_travelled
        if difference > 10:
            print(f'he travelled {distance_travelled} km so he have to travel only {difference}km')
# summary of his travel
print('**** summary ****')
print('number of buildings jumped and selfies posted : ',selfies_posted)
print('no of coffee consumed to regain energy : ',coffee_consumed)
print('remaining energy : ',energy)
print('number of times travelled using bus : ',bus)

"""
OP
#cannot check that for 456 so consider distance as 45km
* if there is any tall buildings press '1' 
 *else press 'any other number'
is there any tall building? 1
distacne travelled by him: 1
* if there is any tall buildings press '1' 
 *else press 'any other number'
is there any tall building? 2
no tall buildings found he has to travell in a bus
distance travelled by him: 11
he travelled 11 km so he have to travel only 34km
* if there is any tall buildings press '1'
 *else press 'any other number'
is there any tall building? 1
distacne travelled by him: 12
* if there is any tall buildings press '1'
 *else press 'any other number'
is there any tall building? 1
distance travelled by him: 13
* if there is any tall buildings press '1'
 *else press 'any other number'
is there any tall building? 2
no tall buildings found he has to travell in a bus
distance travelled by him: 23
he travelled 23 km so he have to travel only 22km
* if there is any tall buildings press '1'
 *else press 'any other number'
is there any tall building? 1
distacne travelled by him: 24
* if there is any tall buildings press '1'
 *else press 'any other number'
is there any tall building? 1
distance travelled by him: 25
* if there is any tall buildings press '1'
 *else press 'any other number'
is there any tall building? 1
distacne travelled by him: 26
* if there is any tall buildings press '1'
 *else press 'any other number'
is there any tall building? 2
no tall buildings found he has to travell in a bus
distance travelled by him: 36
* if there is any tall buildings press '1'
 *else press 'any other number'
is there any tall building? 1
distance travelled by him: 37
* if there is any tall buildings press '1'
 *else press 'any other number'
is there any tall building? 2
no tall buildings found he has to travell in a bus
distance travelled by him: 47
**** summary ****
number of buildings jumped and selfies posted :  7
no of coffee consumed to regain energy :  3
remaining energy :  1
number of times travelled using bus :  4
"""