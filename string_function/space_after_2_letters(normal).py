########## Program 1
#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g
inputString = input("enter the input string:")
i = 0 #counter to track the chars
# intitialize a variable to store the output
newString = ""
while i < len(inputString):
    # to check if the string reached its end
    if (i==len(inputString)-1):
        newString+=inputString[i]
    # if not in its end.
    # add chars to the variable(newstring)
    else:
        newString+=inputString[i]+inputString[i+1]
        newString += " " #add space
    i+=2
print (newString)

"""
OP
enter the input string:abcdefg
ab cd ef g
"""