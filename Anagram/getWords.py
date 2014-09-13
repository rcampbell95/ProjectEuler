def getWords(filename):
	input_file = open(filename,"r")
	# The reason I was thinking we could have the words in a dictionary like this is so that we don't overcheck. 
	data = {'a':[],'b':[],'c':[],'d':[],'e':[],'f':[],'g':[],'h':[],'i':[],'j':[],'k':[],'l':[],'m':[],
          'n':[],'o':[],'p':[],'q':[],'r':[],'s':[],'t':[],'u':[],'v':[],'w':[],'x':[],'y':[],'z':[]}

	currLetter = ord('a')
	for line in input_file:
		if ord(line[0]) != currLetter:
			currLetter += 1
		data[line[0]].append(line)
	input_file.close()
	return(data)