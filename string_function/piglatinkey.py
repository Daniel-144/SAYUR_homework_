########## Program 3
#PigLatin - From the input string, for each word, remove the first, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay ythonPay

# get any sentence as input from the user
inputSentence = input("enter any sentence:")
# initialize a variable to store the piglatin key "ay"
pigLatinKey = 'ay'
# initalized a string to store the converted string
new_sentence=""
for word in inputSentence.split(): #gets the word in a sentence
    # store the fist character in a variable
    first_char=word[0]
    # if it has only one charater word= that charater and piglatin key
    if len(word)<2:
        word=word[0]+pigLatinKey
    # else the other words then first character and piglatinkey
    else:
        word= word[1:] + first_char +pigLatinKey
    new_sentence=new_sentence+" "+word
print(new_sentence)

"""
OP
enter any sentence:i am python
 iay maay ythonpay
"""