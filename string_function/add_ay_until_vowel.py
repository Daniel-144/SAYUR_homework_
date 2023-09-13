########## Program 4
#PigLatin - From the input string, for each word, remove the first chars until a vowek, add it to the end of the word
#and add 'ay' to it.
#eg I am Python
#answer Iay maay nPythoay (in Python 'o' is the first vowel)

inputSentence = input("enter a sentence:")
pigLatinKey = 'ay'
vowels = ['a','e','i','o','u','A','E','I','O','U']
newString=""
for word in inputSentence.split(" "): #to store the words in the string as an iterable list
    #take the first chars until a vowel
    first_vowel_index = 0
    for index, char in enumerate(word): #returns both the index and the char in the word
        #to find the index of the vowel in the word
        if char in vowels:
            first_vowel_index = index
            break
    # word[first_vowel_index+1:] -> the charaters after the vowels(eg: m,n)
    # word[:first_vowel_index+1] -> the charaters before the vowels and the vowel(eg: i,a,pytho)
    newString = newString+word[first_vowel_index+1:]+word[:first_vowel_index+1]+pigLatinKey
    # to add a space after the words
    newString+=" "
print(f"modified string is:{newString}")



"""
OP
enter a sentence:I am Python
modified string is:Iay maay nPythoay 
OP
enter a sentence:Depression Is Just An Illusion
modified string is:pressionDeay sIay stJuay nAay llusionIay 
"""