"""
2. Check if the username and password is correct. 
    Username should contain the char @  and '.com' or '.edu' or '.tech' or 'org' at the end.
    passward is the first, third, and last 3 letters of the username followed by the first three letters of the 
    name of the company mentioned in the username, followed by any 3 numbers.
    eg username : myname@sayur.com. password - mnamesay123 
"""
companyName=input("Enter your company name :") # enter the compant name
middleChar = "@" # initializing special character "@"
while True:    
    name = input("Enter your name & contain the char @ and .com or .edu or .tech or .org at the end :")
    # taking the 0th index char of the company name
    first_let=name[0] 
    # taking the 1st index char of the compant name
    third_let=name[2]   
    # initializing stiring variable for last 3 letters
    lastThreeLetter=""    
    check_name=False
     # this if is 1st it checks "@" in the name and checks name ends with .com or .tech or .edu or .org 
    if name.rfind(middleChar) and (name.endswith(".com") or name.endswith(".edu") or name.endswith(".tech") or name.endswith(".org")):
        # storing the "@" char index
        specialChar_index=name.rfind(middleChar)  
        # storing thr last 3 chars of the name before the char of "@"
        lastThreeLetter=lastThreeLetter+name[specialChar_index-3:specialChar_index] 
        print("While giving password you must give like 1st char of your name,3rd char,and last 3 chars of name before @ special char, 1st 3 chars of your compant name and ends with any three number")
        # entering the password
        password=input("Enter your password : ")    
        # it automatically generate the password
        reference_password=first_let+third_let+lastThreeLetter+companyName[:3]+password[-3:]  
        # if password is same as reference password
        if password in reference_password:  
            # user name and password are correct
            print(f"Correct username {name}")  
            print(f"Correct password {password}")
            break
        else:
            # password is wroung but name is correct
            print(f"Incorrect password {password}. Try again")             
    else:
        # when name not contains @ or ends with .com or .tech or .edu or .org it is invalid name
        print(f"Not a valid user name {name}. Try again")  

"""
Op
Enter your company name :sayur
Enter your name & contain the char @ and .com or .edu or .tech or .org at the end :myname@sayur.tech
While giving password you must give like 1st char of your name,3rd char,and last 3 chars of name before @ special char, 1st 3 chars of your compant name and ends with any three number
Enter your password : mnamesay123
Correct username myname@sayur.tech
Correct password mnamesay123
"""