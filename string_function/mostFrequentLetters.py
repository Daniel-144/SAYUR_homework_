"""
3. Write the function mostFrequentLetters(s), that takes a string s,
and ignoring case (so "A" and "a" are treated the same),
returns a lowercase string containing the letters of s in most frequently used order. 
(In the event of a tie between two letters, follow alphabetic order.)
Eg - "We Attack at Dawn" is input. Output should be 'atwcdekn'
Do not use dictionaries. Try to use string built in functions.
"""
# importing regular expression module
import re
# getting import from the user.
string=input("enter a string:")
# to make the string case insensitive using lower
s=string.lower()
# initializing a list
count=[]
# using regular expression to eliminate numbers and special character 
s=re.sub('[^A-Za-z]+','',s)
# to sort the letters and to eliminate the repeated letters(but saved in a different variable).
sorted_letters=sorted(set(s))
# loop to count how many times the letter is repeated.
for i in range(len(sorted_letters)):
    count.append(s.count(sorted_letters[i]))
# loop to swap the places of the letters with respect to their count.
for num in range(len(count)-1):
    for n in range(len(count)-1):
        if count[n]<count[n+1]:
            sorted_letters[n],sorted_letters[n+1]=sorted_letters[n+1],sorted_letters[n]
            count[n],count[n+1]=count[n+1],count[n]
# joing the list to make it a string.
sorted_letters=''.join(sorted_letters)
print('encoded string:',sorted_letters)
print("count:",count)
"""
OP:
enter a string:We attack at dawn
encoded string: atwcdekn
count: [4, 3, 2, 1, 1, 1, 1, 1]

enter a string:we attack at dawn tomorrow
encoded string: atowrcdekmn
count: [4, 4, 3, 3, 2, 1, 1, 1, 1, 1, 1]
"""