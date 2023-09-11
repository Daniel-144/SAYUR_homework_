#this is a program to calculate the present age using the year of birth
def name_and_age(by, py, nam):
    age = py - by
    print('your name is ', name + ' ' + 'your age is', age)
    print('thank you')



year_of_birth=int(input('enter your year of birth: '))
name=input('enter your name: ')
#i had initialized the present year as 2023
present_year=2023
#if the input is greater than 2023 then the age cannot be calculated because the age of a present cannot be negative
if year_of_birth>present_year:
    print('your name is :', name)
    print('year given is greater than the present year so age cannot be calculated')
#if the year of birth is lesser than the present year we use a function called as name and age to perform the task
else:
    name_and_age(year_of_birth,present_year,name)


"""
OP
enter your year of birth: 2004
enter your name: daniel
your name is  daniel your age is 19
thank you
"""

