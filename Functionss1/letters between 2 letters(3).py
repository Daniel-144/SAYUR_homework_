"""
problem 3:
In the input the first A and last A, print all the letters between those two A.
If there is no A or 2nd A is not found, Find the first B after the first A (if there is a A) and last last B and print all letters between these two B.
If there is no B or 2nd B is not found, Find the first C after the first B (if there is a B) and last last C and print all letters between these two C.
"""
# Finding if there is two alpha present 
def findAlpha(ipstring,alpha):
    if alpha in ipstring:
        return(True)
    else:
        print(f"NO {alpha} found")
        return(False)

def find2Alpha(ipstring,alpha):
    FirstAlpha=ipstring.find(alpha)
    LastAlpha=ipstring.rfind(alpha)
    if FirstAlpha == LastAlpha:
        print(f"only one {alpha} found.")
        return(False)
    else:
        return(True)

def PrintIntermediateLetters(ipstring,alpha):
    FirstAlpha=ipstring.find(alpha)
    LastAlpha=ipstring.rfind(alpha)
    print(f"the letters between the given alphabet {alpha} is : {ipstring[FirstAlpha+1:LastAlpha]}")

def slicingString(ipstring,alpha):
    FirstAlpha=ipstring.find(alpha)
    return(FirstAlpha)



string=input("enter any string:")
alpha=97
for i in range(3):
    if(findAlpha(string,chr(alpha)) == True):
        if(find2Alpha(string,chr(alpha)) == True):
            PrintIntermediateLetters(string,chr(alpha))
            break
        else:
            string=string[slicingString(string,chr(alpha))+1:]
            alpha+=1
    else:
        alpha+=1
        


"""
1)enter any string:as deep as the pacific ocean      
the letters between the given alphabet a is : s deep as the pacific oce

2)enter any string:baby boss
only one a found.
the letters between the given alphabet b is : y 

3)enter any string:computer commerce
NO a found
NO b found
the letters between the given alphabet c is : omputer commer

"""


