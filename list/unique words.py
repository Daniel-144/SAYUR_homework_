"""
from the passage extreact unique words and print them.
accept the passage as an input from the user.
"""

# getting the passage as a input from the user.
passage=input("enter the string:")
# initializing the empty lists to store the number of occourances and the word with only one occurance.
count=[]
unique_word=[]
passage = passage.split(" ") # spliting the words in the passage using split function.
s=set(passage)
# loop to count the number of occuarances of the words in the passage.
for word in s:
    count.append(passage.count(word))
# loop to ceck and append the words with only one occurance.
for no,words in enumerate(s):
    if count[no]==1:
        unique_word.append(words)
    else:
        print(f"'{words}' is not a unique word and it is present in the passage {count[no]} times")
print(f"the unique words are:{unique_word}")

"""
OP
enter the string:don't give up there is no shame in falling down the real shame is not standing up
'up' is not a unique word and it is present in the passage 2 times
'is' is not a unique word and it is present in the passage 2 times
'shame' is not a unique word and it is present in the passage 2 times
the unique words are:['give', "don't", 'falling', 'standing', 'no', 'real', 'there', 'in', 'not', 'the', 'down']
"""