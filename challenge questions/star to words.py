"""
4.Encoding problem - Input is a message and  a pattern. Both strings. Output is the message written in the form
of the pattern. 
Eg -  Message - "I Love India".
      Pattern - "*** **** ** **********     *****"
      Output  - "ILo veIn di aILoveIndi     aILov"
"""
pattern=input("enter the star pattern:")
sting="I Love India "
string=sting.replace(" ","")
sting=list(string)
j=0
pattern=list(pattern)
for i in range(len(pattern)):
    if pattern[i]=="*":
        pattern[i]=string[j]
        j+=1
        if j >=len(string):
            j=0
    else:
        pass
str1=" "
for i in pattern:
    str1 +=i
print(str1)

"""
OP:
enter the star pattern:***** ****** **** *** ***
 ILove IndiaI Love Ind iaI
"""
