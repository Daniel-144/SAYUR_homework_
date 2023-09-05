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