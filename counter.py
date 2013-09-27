import sys, math

if (len(sys.argv) < 2):
	print 'Program executation:\n\t$ python counter.py FILE_NAME > OUTPUT'
	sys.exit(1)

try:
	text = open(sys.argv[1], 'r')
except IOError:
	print '\nIt was not possible to open \''+sys.argv[1]+'\'\n'
	sys.exit(1)

counter = []
totalLetter = 0

for i in range(0,52):
	counter += [0]

biggestWords = [[],[],[],[]]
frequency = [[],[],[],[]]

# Separation of words
for line in text:
	words = line.split(' ')

	for setWord in words:
		setWord = setWord.split('-')
		for word in setWord:
			for letter in word:
				if (ord(letter) >= 65 and ord(letter) <= 90):
					counter[ord(letter) - ord ('A')]+=1
					totalLetter += 1

				if (ord(letter) >= 97 and ord(letter) <= 122):
					counter[ord(letter) - ord ('a')+26]+=1
					totalLetter += 1
			
			word = word.lower()
			
			try:
				while ((word[0] == '.') or (word[0] == ',') or (word[0] == ':') or
					(word[0] == ';') or (word[0] == '!') or (word[0] == '?') or
					word[0] == '\r' or word[0] == '\n' or (word[0] == '\\') or
					(word[0] == '(') or (word[0] == '[') or (word[0] == '{') or
					(word[0] == '-') or (word[0] == '$') or (word[0] == '+') or
					(word[0] == '*') or (word[0] == '/') or (word[0] == '&') or
					(word[0] == '\"') or (word[0] == '_') or (word[0] == '\'') or (word[0] == '~') or
					(word[0] == '\xc2') or (word[0] == '\xb6') or (word[0] == '\x87') or
					(word[0] == '\x86') or (word[0] == '\xc3') or (word[0] == '\xa0') or
					(word[0] == '\xc3') or (word[0] == '\xa6') or (word[0] == '#') or
					(word[0] == '\xa9t') or (word[0] == '\xaat') or (word[0] == '\xef') or
					(word[0] == '\xbb') or (word[0] == '\xbf') or (word[0] == '\xa6i') or
					(word[0] == '\xa6us')):
					word = word[1:]
			except IndexError:
				word = ''

			length = len(word)

			try:
				while ((word[length-1] == '.') or (word[length-1] == ',') or (word[length-1] == ':') or
					(word[length-1] == ';') or (word[length-1] == '!') or (word[length-1] == '?') or
					word[length-1] == '\r' or word[length-1] == '\n' or (word[length-1] == '\\') or
					(word[length-1] == '(') or (word[length-1] == '[') or (word[length-1] == '{') or
					(word[length-1] == ')') or (word[length-1] == ']') or (word[length-1] == '}') or
					(word[length-1] == '-') or (word[length-1] == '$') or (word[length-1] == '+') or
					(word[length-1] == '*') or (word[length-1] == '/') or (word[length-1] == '&') or
					(word[length-1] == '\"') or (word[length-1] == '_') or (word[length-1] == '\'') or
					(word[length-1] == '\xc2') or (word[length-1] == '\xb6') or (word[length-1] == '\x87') or
					(word[length-1] == '\x86') or (word[length-1] == '\xc3') or (word[length-1] == '\xa0') or
					(word[length-1] == '\xc3') or (word[length-1] == '\xa6') or (word[length-1] == '#') or
					(word[length-1] == '\xa9t') or (word[length-1] == '\xaat') or (word[length-1] == '\xef') or
					(word[length-1] == '\xbb') or (word[length-1] == '\xbf') or (word[length-1] == '\xa6i') or
					(word[length-1] == '\xa6us')):
						word = word[:length-1]
						length = len(word)
			except IndexError:
				word = ''

			length = len(word)
			if (length == 2):
				try:
					index = biggestWords[0].index(word)
					frequency[0][index] += 1
				except ValueError:
					biggestWords[0]+= [word.lower()]
					frequency[0] += [1]
			if (length == 3):
				try:
					index = biggestWords[1].index(word)
					frequency[1][index] += 1
				except ValueError:
					biggestWords[1]+= [word.lower()]
					frequency[1] += [1]
			if (length == 4):
				try:
					index = biggestWords[2].index(word)
					frequency[2][index] += 1
				except ValueError:
					biggestWords[2]+= [word.lower()]
					frequency[2] += [1]
			if (length > 4):
				try:
					index = biggestWords[3].index(word)
					frequency[3][index] += 1
				except ValueError:
					biggestWords[3]+= [word.lower()]
					frequency[3] += [1]

print 'Frequency of Letters'
print 'Letter, Frequency'
for i in range(0,52):
	if i < 26:
		print chr(ord('A')+i)+' , '+str(counter[i])
	else:
		print chr(ord('a')+(i-26))+' , '+str(counter[i])

print
print '\tFrequency of Words\n\n'

# Counting words
safeBiggestWords = biggestWords
safeFrequency = frequency

print 'Most Frequent words:'
print '# , Word , frequency'

i = 0
teste = True

while (i < 65 and teste):
	maximum = 0
	level = 0
	# print frequency
	for j in frequency:
		if (maximum < max(j)):
			maximum = max(j)
			level = frequency.index(j)

	if (maximum == []):
		teste = False
	else:
		index = frequency[level].index(maximum)
		print str(i+1)+' , '+biggestWords[level].pop(index)+' , '+str(frequency[level].pop(index))

	i = i+1
print ', Total of words , '+str(len(safeBiggestWords[0])+len(safeBiggestWords[1])+
	len(safeBiggestWords[2])+len(safeBiggestWords[3]))

print
print 'Most Frequent words size #2:'
print '# , Word , frequency'

biggestWords = safeBiggestWords
frequency = safeFrequency

i = 0
teste = True

while (i < 35 and teste):
	maximum = max(frequency[0])

	if (maximum == []):
		teste = False
	else:
		index = frequency[0].index(maximum)
		print str(i+1)+' , '+biggestWords[0].pop(index)+' , '+str(frequency[0].pop(index))

	i = i+1
print ', Total of words , '+str(len(safeBiggestWords[0]))

print
print 'Most Frequent words size #3:'
print '# , Word , frequency'

biggestWords = safeBiggestWords
frequency = safeFrequency

i = 0
teste = True

while (i < 35 and teste):
	maximum = max(frequency[1])

	if (maximum == []):
		teste = False
	else:
		index = frequency[1].index(maximum)
		print str(i+1)+' , '+biggestWords[1].pop(index)+' , '+str(frequency[1].pop(index))

	i = i+1
print ', Total of words , '+str(len(safeBiggestWords[1]))

print
print 'Most Frequent words size #4:'
print '# , Word , frequency'

biggestWords = safeBiggestWords
frequency = safeFrequency

i = 0
teste = True

while (i < 35 and teste):
	maximum = max(frequency[2])

	if (maximum == []):
		teste = False
	else:
		index = frequency[2].index(maximum)
		print str(i+1)+' , '+biggestWords[2].pop(index)+' , '+str(frequency[2].pop(index))
	i = i+1
print ', Total of words , '+str(len(safeBiggestWords[2]))

print
print 'Most Frequent bigrams:'
print '# , Bigram , frequency'

biggestWords = safeBiggestWords
frequency = safeFrequency
bigrams = []
frequencyBigrams = []

trash = biggestWords.pop(0)

for i in biggestWords:
	for word in i:
		for j in range(0,len(word)-1):
			bigram = word[j]+word[j+1]
			try:
				index = bigrams.index(bigram)
				frequencyBigrams[index] += 1
			except ValueError:
				bigrams += [bigram]
				frequencyBigrams += [1]

bigramsSize = len(bigrams)

i = 0
teste = True

while (i < 35 and teste):
	maximum = max(frequencyBigrams)

	if (maximum == []):
		teste = False
	else:
		index = frequencyBigrams.index(maximum)
		print str(i+1)+' , '+bigrams.pop(index)+' , '+str(frequencyBigrams.pop(index))
	i = i+1
print ', Total of words , '+str(bigramsSize)
	
print
print 'Most Frequent Trigrams:'
print '#, Trigram , frequency'

trigrams = []
frequencyTrigrams = []

trash = biggestWords.pop(0)

for i in biggestWords:
	for word in i:
		for j in range(0,len(word)-2):
			trigram = word[j]+word[j+1]+word[j+2]
			try:
				index = trigrams.index(trigram)
				frequencyTrigrams[index] += 1
			except ValueError:
				trigrams += [trigram]
				frequencyTrigrams += [1]

trigramsSize = len(trigrams)

i = 0
teste = True

while (i < 35 and teste):
	maximum = max(frequencyTrigrams)

	if (maximum == []):
		teste = False
	else:
		index = frequencyTrigrams.index(maximum)
		print str(i+1)+' , '+trigrams.pop(index)+' , '+str(frequencyTrigrams.pop(index))
	i = i+1

print ', Total of words , '+str(trigramsSize)