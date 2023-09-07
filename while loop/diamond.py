######## Problem 1 ###############
#Write a program that prints out a diamond shape using $.
#After printing each line, wait for user input. If the user presses space, continue
#If the users presses any other key, stop printing. Maximum 10 lines

lines=int(input("enter the number of lines (less than or equal to 5)"))
number,i=1,1

if lines <= 5:
    while number <= lines:
        choice=input("enter space to print diamond pattern:")
        if choice==" ":
            print(" "*(lines-number),end="")
            print(f"{'$ '*number}",end="")
            number +=1
        else:
            break
        print()
    while lines > 0:
        choice=input("enter space to print diamond pattern:")
        if choice==" ":
            print(" "*(i),end="")
            print(f"{'$ '*(lines-i)}",end=" ")
            i+=1
        else:
            break
        print()
else:
    print("maximum lines is 10")


    



    
        
