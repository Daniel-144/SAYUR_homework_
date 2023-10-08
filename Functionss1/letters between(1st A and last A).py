"""
find the letters between the first a and last a and print them.
"""

# function to print the first a and last a and print the intermediate letters
def theLettersBetweenFirstAandLastA(string,alpha):
    if "a" in string:
        FirstAIndex=string.find(alpha)
        LastAIndex=string.rfind(alpha)
        if (FirstAIndex == LastAIndex):
            print("no letters between first A and Last A.")
        else:
            print(string[FirstAIndex+1:LastAIndex])
    else:
        print("There is No A in the given string.")

    


   
inputString=input("enter any string:")
alpha="a"
# calling the function to  print the intermediate letters.
theLettersBetweenFirstAandLastA(inputString,alpha)



