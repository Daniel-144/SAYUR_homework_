# Input is a sentence. Find the number of times each word appears.
def no_of_words(sentence):
    count=1
    for i in sentence :
        if i=="":
            count+=1
    return (count)

sentence=input("enter any sentence")
words=no_of_words(sentence)
print("the number of words in the sentence=",words)
