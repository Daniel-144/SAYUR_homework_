# Calcualte and print which standard the student is studying - Write a program to ask the user for his/her name
#and print 'Hello', user's name.
#Ask what year they were born.
#eg Hello Chitra, what year were you born?
#get the year from the user.
#alculate if the user is going to elementary school, middle school, highschool or college, based on users age.
#(hint - use if/elif)
def level_of_education(x):
    if x < 5:
        return('you cannot be enrolled in school !')
    elif x<6 :
        return ('you are in kindergarten. ')
    elif  x<12:
        return('you are in elementary school. ')
    elif x<15:
        return('you are in middle school .')
    elif x<19:
        return('you are in high school .')
    else:
        return('you are in college or graduated')

user_name=input('enter your name : ')
year_of_birth= int(input(f'hello {user_name} , enter the year you were born : '))
present_year=2023
if(year_of_birth > present_year):
    print('hello '+ user_name +', the year you have entered is invalid')
else:
    age = present_year - year_of_birth
    print('your age is : ',age)
    education_level= level_of_education (age)
    print(education_level)

