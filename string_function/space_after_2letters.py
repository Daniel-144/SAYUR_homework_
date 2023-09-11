########## Program 1
#Get an input string from the user. Add a space at every 3rd char.
#eg input = abcdefg , output = ab cd ef g
inputString = input("enter the string:")
i = 0 #counter to track the chars
newString = ""
while i < len(inputString):
    newString += i
    newString +
    newString += " " 
    i+=2
#check to add the chars at the end
#FillinMissingCode

print (newString)