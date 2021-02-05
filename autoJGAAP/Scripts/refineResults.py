
import sys
import re


#passed experiment text, return real author
def getAuthor(exp):
	author = re.search("Documents/Unknown/.+?/", exp)
	if author != None:
		author = author.group(0)[18:-1]
	return author

#passed experiment text, return #1 guess
def getAttempt(exp):
	attempt = re.search("1. .+? [0-9]\.[0-9]", exp)
	if attempt != None:
		attempt = attempt.group(0)[3:-4]
	return attempt

#passed experiment text, return dictionary {category : [settings,]}
#:category" as in Canonicizer, Event Driver, etc
def getExpInfo(exp):
	setD = {}
	net = re.search("Canonicizers: \n(.+?\n)+EventDrivers:", exp)
	if net != None: 
		tsL = net.group(0)[15:-15].replace('        ','').replace(',',';').split(' \n')
		setD["Canonicizers"] = tsL

	net = re.search("EventDrivers: \n(.+?\n)+Analysis:", exp)
	if net != None: 
		tsL = net.group(0)[15:-11].replace('        ','').replace(',',';').split(' \n')
		setD["EventDrivers"] = tsL

	net = re.search("Analysis: \n(.+?\n)+?1.", exp)
	if net != None: 
		both = net.group(0)[11:-4].replace('        ','').replace(',',';')	#line contains both analysis method and distance function
		thisL = both.split(" with ")
		setD["Analysis"] = thisL[0]
		setD["DistanceFunction"] = thisL[1]

	return setD

#================================================================

path = sys.argv[1]
dest = sys.argv[2]

with open(path) as file:
	text = file.read()

noneL = []	#list of text blocks the script failed to find an author in
setD = {} 	#dictionary of this experiment's settings
setDL = [] 	#list of all exp setting dicts
recordD = {} #dictionary {str(setD) : [correct, total]}
for exp in text.split("\n\n\n")[:-1]:	#skip empty final entry
	author = getAuthor(exp)
	attempt = getAttempt(exp)

	if author == attempt:
		correctness = 1
	else:
		correctness = 0

	if author != None and attempt != None:
		setD = getExpInfo(exp)
		setD['Author'] = author
		thisExp = str(setD)
		if setD not in setDL:
			setDL.append(setD)

		if thisExp not in recordD:
			recordD[thisExp] = [correctness, 1]
		else:
			recordD[thisExp][0] += correctness		#[0] = number correct
			recordD[thisExp][1] += 1				#[1] = number attempted

	else:
		noneL.append(exp)



#final output
with open(dest, 'w') as file:
	file.write('True Author,Canonicizer,Event Driver,Analysis Method,Distance Function,Correct,Attempted,Success Rate\n')
	for di in setDL:
		file.write(di['Author']+',')
		file.write('&'.join(di["Canonicizers"])+',')
		file.write('&'.join(di["EventDrivers"])+',')
		file.write(di["Analysis"]+',')
		file.write(di["DistanceFunction"]+',')
		file.write(str(recordD[str(di)][0]) + ',' + str(recordD[str(di)][1])+',')
		file.write(str(recordD[str(di)][0] / recordD[str(di)][1])+'\n')

if noneL:
	with open("author_error.txt", 'w') as file:
		for element in noneL:
			file.write(element + '\n')















