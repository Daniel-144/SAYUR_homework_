"""
2. from a given passage find the longest and shortest word.
and print the same. accept the passage as an input from the user.
"""

passage=input("enter the string:")
# spliting the passage using the split function
passage=passage.split(" ")
# initializing the longest word and the shortest word as none.
smallest_word=None
longest_word=None
# loop to find the smallest and longest word in the passage.
for word in passage:
    word_length=len(word)
    # if the smallest word is null and the length of the word is smaller than that of the smallest word found.
    if (smallest_word is None) or (word_length < len(smallest_word)):
        smallest_word = word
    # if the largest word is null and the length of the word is greater than that of the longest word found word found.
    if (longest_word is None) or (word_length > len(longest_word)):
        longest_word=word
print("the smallest word in the passage is:",smallest_word)
print("the longest word in the passage is:",longest_word)


"""
OP
enter the string:The difference between a novice and a master is that a master has failed more times than a novice had tried.  
the smallest word in the passage is: a
the longest word in the passage is: difference
"""
