"""
1. Print the level of the password security and if the password is acceptable
    Weak - only alphabets or only numbers or only special chars
    Ok - at least one alphabet, one number and one special char
    strong - at least three alphabets, two numbers and one special char
    Very strong - same as strong, but at least 16 count

    All passwords must be at least 8 chars long. You can use RegEx if you want.
"""
# initializing list to count the numbert of special characters and number
numbers=['1','2','3','4','5','6','7','8','9','0']
specialChar=['~','`','!','@','#','$','%','^','&','*','?','<','>',':',';','|','/','{','}']
# loop to get a strong password( loop will execute until the user enters a strong password)
while(True):
    # counter for number
    numCount=0
    # counter for special character.
    specialCharCount=0
    # variable to store the input entered by the user
    password=input("enter your password:")
    # password should not contain space so we use if statement to reject the password with space
    if " " in password:
        print("password should not contain a space")
        print("try again")
    # average minimum password length.
    if len(password) < 8:
        print("password is too short")
        print("try again")
    # average maximum password length
    elif len(password) > 127:
        print("password is too long")
        print("try again")
    else:
        # loop to count the number of special character
        for i in password:
            if i in specialChar:
                specialCharCount+=1
        # if statement to check if the password contains only one type of character(character or integer or special character).
        if password.isalpha() == True or password.isdigit() == True or specialCharCount==len(password):
            print("Password strength:'weak'")
            print("try again")
        else:
            # loop to count the number of integers present in the password
            for char in password:
                if char in numbers:
                    numCount+=1
            # to find the number of character
            charCount=len(password)-(specialCharCount+numCount)
            # determing the strength of the characters
            if specialCharCount==0:
                print('password strength:weak')
                print("try again")
            if charCount >=1 and numCount ==1 and specialCharCount == 1:
                print("password strength:Ok")
            elif charCount>=3 and numCount>=2 and specialCharCount>=1:
                if len(password)<16:
                    print("password strength:strong")
                    break
                else:
                    print("password strength: Very Strong")
                    break


        



    

  



    