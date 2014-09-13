from getWords import * # importing the getWords(filename) function

def findChar(string, char):
	length = len(string)
	for count in range(0, length):
		if string[count] == char:
			return count
		count += 1
	return -1

def isSubString(wordToCheck, subString): # This function checks to see if a word is found
	cpyWordToCheck = wordToCheck         # in another word
	for char in subString:
		if char not in cpyWordToCheck:
			return False
		elif char in cpyWordToCheck:
			indexChar = findChar(cpyWordToCheck, char)
			# This part takes out the found character by splitting the word into two parts and
			# concatenating(sticking them together) them ex: if the character 'g' is found in 'anagram'
			# it will add 'ana' and 'ram', making 'anaram'
			cpyWordToCheck = cpyWordToCheck[:indexChar] + cpyWordToCheck[indexChar + 1:]
	return True

data = getWords("wordsEn.txt")

wordToAnagram = input(">") # Or raw_input("> "), for Python 2.7

anagram = ''
for word in data[wordToAnagram[0]]:
	# Removing the newline character from the end of all the words
	# Otherwise, isSubString() doesn't work
	word = word[0:-1]

	# A check to make sure the substring isn't the word itself
	if wordToAnagram != word:
		found = isSubString(wordToAnagram, word)
	if found == True:
		anagram += word
		break

print(anagram)
		


