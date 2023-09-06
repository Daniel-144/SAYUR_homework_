######## Problem 1 ###############
#Write a program that prints out a diamond shape using $.
#After printing each line, wait for user input. If the user presses space, continue
#If the users presses any other key, stop printing. Maximum 10 lines

lines=int(input("enter the number of lines"))
number=1
count=0
if lines <=10:
    while(number<=lines//2):
        choice=input("enter space to print:")
        if choice ==" " and count<=5:
            print(" "*((lines//2)-number),end="")
            print(f"{'$ '*number}",end=" ")
            number+=1
            count+=1
        else:
          break
        print()
    n=1
    while(n<=lines//2):
        choice=input("enter space to print:")
        if choice==" " and count<=10:
            print(" "*(n),end="")
            print(f"{'$ '*((lines//2)-n)}",end=" ")
            n+=1
            count+=1
        else:
            break
        print()
else:
    print("maximum number of lines is 10.")
    



    
        
