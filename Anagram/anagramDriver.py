import anagram

# testing findChar()
word = 'anagram'
# list of return values for findChar
posChar = [0,1,0,3,4,0,6]
count = 0
for char in word:
	assert(anagram.findChar(word, char) == posChar[count])
	count += 1

# testing isSubString()

# To test more values, just add more words to check and substrings
# and also make sure the number being compared to the count
# in the if statement is greater than all the words that should be true 
wordsToCheck = ['anagram', 'draw', 'keep', 'reach']
subStrings = ['gram', 'ward', 'peek', 'teach']

for count in range(0,len(wordsToCheck):
	found = anagram.isSubString(wordsToCheck[count],subStrings[count])
	if count < 3: 
		# assert gives you an error if found is false
		assert(found)
	else:
    # The last one should be false
		assert(not(found))