########## Program 1
#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g
inputString = input("enter a string:")
i = 0 #counter to track the chars
newString = ""
inputString=list(inputString)
# loop for adding space after 2 characters.
for letter in inputString:
    if (i%2)==0:
        newString=newString+" "+letter
        i=i+1
    else:
        newString=newString+letter
        i+=1
print(newString)

"""
OP
enter the input string:abcdefg
 ab cd ef g
"""