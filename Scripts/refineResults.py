
import sys
import re


#passed experiment text, return real author
def getAuthor(exp):
	author = re.search("by .+? Documents/", exp)
	if author != None:
		author = author.group(0)[3:-11]
	return author

#passed experiment text, return #1 guess
def getAttempt(exp):
	attempt = re.search("1. .+? [0-9]\.[0-9]{5}", exp)
	if attempt != None:
		attempt = attempt.group(0)[3:-8]
	return attempt

#passed experiment text, return dictionary {category : [settings,]}
#:category" as in Canonicizer, Event Driver, etc
def getExpInfo(exp):
	catD = {}
	net = re.search("Canonicizers: \n(.+?\n)+EventDrivers:", exp)
	if net != None: 
		tsL = net.group(0)[15:-15].replace('        ','').replace(',',';').split(' \n')
		catD["Canonicizers"] = tsL

	net = re.search("EventDrivers: \n(.+?\n)+Analysis:", exp)
	if net != None: 
		tsL = net.group(0)[15:-11].replace('        ','').replace(',',';').split(' \n')
		catD["EventDrivers"] = tsL

	net = re.search("Analysis: \n(.+?\n)+1.", exp)
	if net != None: 
		both = net.group(0)[11:-4].replace('        ','').replace(',',';')	#line contains both analysis method and distance function
		thisL = both.split(" with ")
		catD["Analysis"] = thisL[0]
		catD["DistanceFunction"] = thisL[1]

	return catD

#================================================================

path = sys.argv[1]
dest = sys.argv[2]

with open(path) as file:
	text = file.read()

noneL = []	#list of text blocks the script failed to find an author in
catD = {} #dictionary of this experiment's settings
catDL = [] #list of all exp setting dicts
recordD = {} #dictionary {str(catD) : [correct, total]}
for exp in text.split("\n\n\n"):
	author = getAuthor(exp)
	attempt = getAttempt(exp)

	if author == attempt:
		correctness = 1
	else:
		correctness = 0

	if author != None and attempt != None:
		catD = getExpInfo(exp)
		catD['Author'] = author
		thisExp = str(catD)
		if catD not in catDL:
			catDL.append(catD)

		if thisExp not in recordD:
			recordD[thisExp] = [correctness, 1]
		else:
			recordD[thisExp][0] += correctness
			recordD[thisExp][1] += 1

	else:
		noneL.append(exp)



#final output
with open(dest, 'w') as file:
	file.write('True Author,Canonicizer,Event Driver,Analysis Method,Distance Function,Correct,Attempted,Success Rate\n')
	for di in catDL:
		file.write(di['Author']+',')
		file.write('&'.join(di["Canonicizers"])+',')
		file.write('&'.join(di["EventDrivers"])+',')
		file.write(di["Analysis"]+',')
		file.write(di["DistanceFunction"]+',')
		file.write(str(recordD[str(di)][0]) + ',' + str(recordD[str(di)][1])+',')
		file.write(str(recordD[str(di)][0] / recordD[str(di)][1])+'\n')















