# Get two names. If the length of the two names is not equal, add 'a' at the end of the short name
# until the length is equal.
# Eg - input - cat, arrow. (legnth is not equal)
# Output - cataa, arrow (length is equal by adding a)

#function to calculate the length of the string(can use length insted)
def length_of_string1(string_1):
    count=0
    for i in string_1:
        count+=1
    return count
#functon to calculate the length of the string 2
def length_of_string2(string_2):
    count=0
    for j in string_2:
        count+=1
    return count


string_1=input('enter any word:')
string_2=input('enter any word:')
length_1=length_of_string1(string_1)
print(length_1)
length_2=length_of_string2(string_2)
print(length_2)
# if 2 length are equal no need to equalize
if(length_1 == length_2):
    print("no need to add 'a' string 1= "+ string_1 +" and string 2 is "+string_2)
#if length of str1 then add a until both strings are equal
elif length_1 > length_2 :
    while length_1 >length_2 :
        string_2=string_2 +"a"
        length_2 +=1
    print("the reordered version of name2 is "+string_2+" and name 1 is "+string_1)
#if length of str2 then add a until both strings are equal
else:
    while length_2 >length_1 :
        string_1=string_1 +"a"
        length_1 +=1
    print("the reordered version of name1 is "+string_1+" and name 2 is "+string_2)

    """
    OP
    enter any word:virat 
enter any word:ronaldo
5
7
the reordered version of name1 is virataa and name 2 is ronaldo
"""


