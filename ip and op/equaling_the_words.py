# Get two names. If the length of the two names is not equal, add 'a' at the end of the short name
# until the length is equal.
# Eg - input - cat, arrow. (legnth is not equal)
# Output - cataa, arrow (length is equal by adding a)
def length_of_string1(string_1):
    count=0
    for i in string_1:
        count+=1
    return count
def length_of_string2(string_2):
    count=0
    for j in string_2:
        count+=1
    return count


string_1=input('enter any word')
string_2=input('enter any word')
length_1=length_of_string1(string_1)
print(length_1)
length_2=length_of_string2(string_2)
print(length_2)
if(length_1 == length_2):
    print("no need to add 'a' string 1= "+ string_1 +" and string 2 is "+string_2)
elif length_1 > length_2 :
    while length_1 >length_2 :
        string_2=string_2 +"a"
        length_2 +=1
    print("the reordered version of name2 is "+string_2+" and name 1 is "+string_1)
else:
    while length_2 >length_1 :
        string_1=string_1 +"a"
        length_1 +=1
    print("the reordered version of name2 is "+string_1+" and name 1 is "+string_2)


