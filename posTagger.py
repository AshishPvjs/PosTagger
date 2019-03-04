#Submitted By: Ashish Peruri
#email: vperur2@uic.edu

def toTagList(s):
	"""
	Splits a given String with tags into a List of List in the form [word, tag]
	A tag /ST is given to <s> i.e Start Tag
	A tag /ET is given to </s> i.e End Tag
	"""
	stuples = s.split()
	taglist = []
	for i in stuples:
		if(i == "<s>"):
			taglist.append([i,"ST"])
		elif(i == "</s>"):
			taglist.append([i,"ET"])
		else:
			taglist.append(i.split("/"))
	return taglist

def countWordTagOccurence(word,tag,taglist):
	"""
	Counts The Occurence of a Given Word and Given Tag 
	"""
	count = 0.0
	for i in taglist:
		if i[0]==word and i[1]==tag:
			count+=1.0
	return count

def countTagOccurence(tag1,tag2,taglist):
	"""
	Counts the Occurence of Tag2 after Tag1
	"""
	count = 0.0
	l = len(taglist)
	for i in range(1,l):
		if tag1 == taglist[i-1][1] and tag2 == taglist[i][1]:
			count += 1.0
	return count

def findBigramProbabilities(testTagList,tagdict,trainTagList):
	"""
	Returns a List of Lists Containing both the bigram and tag probabilities
	"""
	# print(testTagList)
	l = len(testTagList)
	res = []
	bigram = []
	for i in range(0,l):
		x = countWordTagOccurence(testTagList[i][0],testTagList[i][1],trainTagList)
		y = tagdict[testTagList[i][1]]
		bigram.append([x,y])
	# print(bigram)
	tagProb = []
	for i in range(1,l):
		x = countTagOccurence(testTagList[i-1][1],testTagList[i][1],trainTagList)
		y = tagdict[testTagList[i-1][1]]
		tagProb.append([x,y])
	# print(tagProb)
	res.append(bigram)
	res.append(tagProb)
	return res

def probOfString(bigramProb):
	"""
	Returns the Probabilities
	"""
	resProb = 1.00000000000
	for i in bigramProb:
		for j in i:
			if j[0] == 0:
				return 0
			resProb *= j[0]/j[1]
	return resProb

def showBigramProbabilities(res,teststring):
	"""
	Just Prints an output showing the bigram probabilities
	"""
	bi = res[0]
	ta = res[1]
	# for i,j in enumerate(teststring):
	# 	print("P("+j[0]+"|" + j[1]+ ") = "),
	# 	print(bi[i][0]/bi[i][1])
	l = len(teststring)
	file = open("CorpusProb.txt","w+")
	for i in range(1,l-1):
		# print("P("+teststring[i][0]+"|" + teststring[i][1]+ ") = "),
		# print(bi[i][0]/bi[i][1]),
		# print("and"),
		# print("P("+teststring[i][1]+"|" +teststring[i-1][1]+ ") = "),
		# print(ta[i][0]/ta[i][1])
		file.write("P("+teststring[i][0]+"|" + teststring[i][1]+ ") = ")
		file.write(str(bi[i][0]/bi[i][1]))
		# file.write("and")
		file.write("  and P("+teststring[i][1]+"|" +teststring[i-1][1]+ ") = ")
		file.write(str(ta[i][0]/ta[i][1])+"\n")
	# print("P("+teststring[l-1][0]+"|" + teststring[l-1][1]+ ") = "),
	# print(bi[l-1][0]/bi[l-1][1])
	file.write("P("+teststring[l-1][0]+"|" + teststring[l-1][1]+ ") = ")
	file.write(str(bi[l-1][0]/bi[l-1][1]))
	file.close()

if __name__ =="__main__":
	s = """<s> sitting/VBG up/RP now/RB langdon/VBP frowned/JJ at/IN his/PRP$ bedside/JJ guest/NN relations/NNS handbook/NN whose/WP$ cover/NN boasted/VBD sleep/NN like/IN a/DT baby/NN in/IN the/DT city/NN of/IN lights/NNS </s>
	<s> slumber/VB at/IN the/DT paris/JJ ritz/NN </s>
	<s> he/PRP turned/VBD and/CC gazed/VBD tiredly/RB into/IN the/DT full/JJ length/NN mirror/NN across/IN the/DT room/NN </s>
	<s> the/DT man/NN staring/VBG back/RB at/IN him/PRP was/VBD a/DT stranger/NN tousled/JJ and/CC weary/JJ </s>
	<s> you/PRP need/VBP a/DT vacation/NN robert/NN </s>
	<s> the/DT past/JJ year/NN had/VBD taken/VBN a/DT heavy/JJ toll/NN on/IN him/PRP but/CC he/PRP did/VBD not/RB appreciate/VB seeing/VBG proof/NN in/IN the/DT mirror/NN his/PRP$ usually/RB sharp/JJ blue/JJ eyes/NNS looked/VBN hazy/RB and/CC drawn/VBN tonight/NN </s>
	<s> a/DT dark/JJ stubble/NN was/VBD shrouding/VBG his/PRP$ strong/JJ jaw/NN and/CC dimpled/NN chin/NN </s>
	<s> around/IN his/PRP$ temples/NNS the/DT gray/JJ highlights/NN were/VBD advancing/VBG making/VBG their/PRP$ way/NN deeper/RBR into/IN his/PRP$ thicket/NN of/IN coarse/JJ black/JJ hair/NN </s>
	<s> although/IN his/PRP$ female/JJ colleagues/NNS insisted/VBD the/DT gray/JJ only/JJ accentuated/NN his/PRP$ bookish/JJ appeal/NN langdon/NN knew/VBD better/RBR </s>
	<s> if/IN boston/NN magazine/NN could/MD see/VB me/PRP now/RB </s>
	<s> last/JJ month/NN much/RB to/TO langdon/NN s/VBZ embarrassment/NN boston/NN magazine/NN had/VBD listed/VBN him/PRP as/IN one/CD of/IN that/WDT city/NN s/PRP top/VBP ten/CD most/RBS intriguing/JJ people/NNS a/DT dubious/JJ honor/NN that/WDT made/VBD him/PRP the/DT brunt/NN of/IN endless/JJ ribbing/NN by/IN his/PRP$ harvard/JJ colleagues/NNS </s>
	<s> tonight/RB three/CD thousand/CD miles/NNS from/IN home/NN the/DT accolade/NN had/VBD resurfaced/VBN to/TO haunt/VB him/PRP at/IN the/DT lecture/NN he/PRP had/VBD given/VBN </s>
	<s> ladies/NNS and/CC gentlemen/NNS the/DT hostess/NNS had/VBD announced/VBN to/TO a/DT full/JJ house/NN at/IN the/DT american/NN university/NN of/IN paris/NNS s/VBZ pavilion/NN dauphine/NN </s>
	<s> Our/PRP$ guest/NN tonight/NN needs/VBZ no/DT introduction/NN </s>
	<s> he/PRP is/VBZ the/DT author/NN of/IN numerous/JJ books/NNS the/DT symbology/NN of/IN secret/NN sects/VBZ the/DT an/DT of/IN the/DT illuminati/NN the/DT lost/VBN language/NN of/IN ideograms/NNS and/CC when/WRB i/FW say/VBP he/PRP wrote/VBD the/DT book/NN on/IN religious/JJ iconology/NN i/NNS mean/VBP that/DT quite/RB literally/RB </s>
	<s> many/JJ of/IN you/PRP use/VBP his/PRP$ textbooks/NNS in/IN class/NN </s>
	<s> langdon/NN forced/VBD an/DT awkward/JJ smile/NN </s>"""
	trainTagList = toTagList(s)
	#A dictionary used to store tags and their counts
	tagdict = {}
	for i in trainTagList:
		try:
			tagdict[i[1]] +=1
		except KeyError:
			tagdict[i[1]] = 1
	#A dictionary used to store words and their counts
	worddict = {}
	for i in trainTagList:
		try:
			worddict[i[0]] +=1
		except KeyError:
			worddict[i[0]] = 1
	tests = " <s> langdon frowned at the author of numerous books </s>"
	ss = tests.split()
	possibletags = [[] for i in range(len(ss))]
	finaltags=[[]]
	for i,k in enumerate(ss):
		for j in trainTagList:
			if k == j[0] and j[1] not in possibletags[i]:
				possibletags[i].append(j[1])
	for i in possibletags:
		finaltags = [ x + [y] for y in i for x in finaltags]
	# print(finaltags)
	lfinal = len(finaltags)
	testStrings = [[] for i in range(lfinal)]
	for i in range(lfinal):
		for j in range(len(ss)):
			testStrings[i].append([ss[j],finaltags[i][j]])
	# print(testStrings)
	if(len(testStrings)!=0):

		print("Possible Tags Are:")
		print(testStrings)
		print("\n \n \n \n After Calculating the results")
		finalProbalities = []
		train_res = findBigramProbabilities(trainTagList,tagdict,trainTagList)
		# print(train_res)
		showBigramProbabilities(train_res,trainTagList)
		for testString in testStrings:
			res = findBigramProbabilities(testString,tagdict,trainTagList)
			prob = probOfString(res)
			finalProbalities.append([testString,prob])

		maxProb = finalProbalities[0][1]
		index = 0
		for i,j in enumerate(finalProbalities):
			if maxProb < j[1]:
				maxProb = j[1]
				index = i
		print("The result which has the maximum likelihood is "),
		print(finalProbalities[i][0])

		print("The Probability is"),
		print(finalProbalities[i][1])
	else:
		print("The inputed test string has a bigram probability zero somewhere")

#Submitted By : Ashish Peruri
#email: vperur2@uic.edu
