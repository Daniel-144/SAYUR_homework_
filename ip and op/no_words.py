# Input is a sentence. Find the number of times each word appears.

#function to find the number of words
def no_of_words(sentence):
    count=1
    for i in sentence :
        if i==" ":
            count+=1
    return (count)
# input from the usser
sentence=input("enter any sentence:")
words=no_of_words(sentence)
# output
print("the number of words in the sentence=",words)

"""
OP
enter any sentence:hi buddy how are you
the number of words in the sentence= 5
"""