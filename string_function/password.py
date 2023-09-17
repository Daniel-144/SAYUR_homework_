"""
1. Print the level of the password security and if the password is acceptable
    Weak - only alphabets or only numbers or only special chars
    Ok - at least one alphabet, one number and one special char
    strong - at least three alphabets, two numbers and one special char
    Very strong - same as strong, but at least 16 count

    All passwords must be at least 8 chars long. You can use RegEx if you want.
"""
import re
# loop to get a strong password( loop will execute until the user enters a strong password)
while(True):
    # variable to store the input entered by the user
    password=input("enter your password:")
    # counter for special character.
    specialCharCount=len(re.findall(r'[^a-zA-Z0-9]',password))
     # counter for number
    numCount=len(re.findall(r'[0-9]',password))
    # to find the number of character
    charCount=len(re.findall(r'[A-za-z]',password))
    # password should not contain space so we use if statement to reject the password with space
    if " " in password:
        print("password should not contain a space")
        print("try again")
    # average minimum password length.
    if len(password) < 8:
        print("password is too short")
        print("try again")
    # average maximum password length
    #Typical maximum length is 128 characters.
    elif len(password) >= 128:
        print("password is too long")
        print("try again")
    else:
        # if statement to check if the password contains only one type of character(character or integer or special character).
        if password.isalpha() == True or password.isdigit() == True or specialCharCount==len(password):
            print("Password strength:'weak'")
            print("try again")
        else:
            # determing the strength of the characters
            # assuming the special case(not given in the question)as zero.
            if specialCharCount == 0 or numCount == 0:
                print('password strength:weak')
                print("try again")
            elif charCount>=3 and numCount>=2 and specialCharCount>=1:
                if len(password)<16:
                    print("password strength:strong")
                    break
                else:
                    print("password strength: Very Strong")
                    break
            else:
                print("password strength:Ok")
                print("try again")

"""
enter your password:Daniel123
password strength:weak
try again
enter your password:d123456@123
password strength:Ok
try again
enter your password:Daniel@123
password strength:strong
"""
        



    

  



    