#Luke De Vos
#EVL Labs
#Settings config file writer


import sys

setD = {0:[], 1:[], 2:[], 3:[], 4:[], 5:[]}

path = sys.argv[1]
dest = sys.argv[2]

isFirstLine=True
expSetName=""
with open(path) as file:
	for line in file:
		lineL = line[0:-1].split(',') #trim trailing newline
		if isFirstLine:
			expSetName = lineL[0]
			isFirstLine = False
		else:
			for i in range(len(lineL)):
				if lineL[i] != "":
					setD[i].append(lineL[i])

with open(dest, 'w') as file:
	file.write(expSetName+'\n')
	for a in setD[0]:
		for b in setD[1]:
			for c in setD[2]:
				for d in setD[3]:
					for e in setD[4]:
						for f in setD[5]:
							file.write(a+','+b+','+c+','+d+','+e+','+f+'\n')	







