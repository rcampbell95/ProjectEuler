from getWords import * # importing the getWords(filename) function

def isSubString(subString, wordToCheck): # This function checks to see if a word is foun
    cpyWordToCheck = wordToCheck         # in another word
    for char in subString:
        if char not in cpyWordToCheck:
            return False
        else if char in cpyWordToCheck:
            # I was thinking of removing characters that were already found
            # so that errors don't happen with words with more than one
            # of a letter.
        return True
        

data = getWords("wordsEn.txt")

word = input("> ") # Or raw_input("> "), for Python 2.7

count = ord('a')
print(count)
for words in data[chr(count)]:
    for word in words:
        pass # This doesn't do anything
    
