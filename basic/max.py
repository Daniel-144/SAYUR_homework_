num_1=int(input('enter the value of number 1 : '))
num_2=int(input('enter the value of number 1 : '))
num_3=int(input('enter the value of number 1 : '))
print('enter 1 if u want to get the maximum number \n enter 0 if you want to find the minimum number')
choice=int(input('enter your choice'))
if(choice==1):
    if num_1==num_2 or num_3==num_1:
        print("cannot find the maximum number because some values are equal")
    elif num_1>num_2 and num_1>num_3:
        print('number 1 is the maximum number :',num_1)
    elif num_2>num_1 and num_2>num_3:
        print('number 1 is the maximum number :',num_2)
    elif num_3>num_2 and num_3>num_1:
        print('number 1 is the maximum number :',num_3)
elif(choice==0):
    if num_1==num_2 or num_3==num_1:
        print("cannot find the minimum number because some values are equal")
    elif num_1<num_2 and num_1<num_3:
        print('number 1 is the minimum number :',num_1)
    elif num_2<num_1 and num_2<num_3:
        print('number 1 is the minimum number :',num_2)
    elif num_3<num_2 and num_3<num_1:
        print('number 1 is the minimum number :',num_3)
else:
    print('invalid input')
