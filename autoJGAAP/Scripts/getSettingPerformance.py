#Luke De Vos

#Find which settings most consistently positively influence the experiments they are a part of

import re
import sys
import statistics
import time

#compute mean, median for each experiment setting
#overwrites
#reduced lists: [number of experiments with this setting, mean success % of experiments with this setting, standard deviation, and median success rate of experiments with this setting]
def reduce(li):
	total=0
	for entry in li:
		total += entry
	expCount = len(li)
	avg = round(total / expCount, 6)
	dev=0
	if len(li) > 1:
		dev = round(statistics.stdev(li), 6)
	median = li[int(expCount/2)]
	return [expCount, avg, dev, median]


#MAIN
sRateIndex = 7 #column with experiments' success rates
path = sys.argv[1]
dest = sys.argv[2]
if len(sys.argv) > 1:
	path = sys.argv[1]

#populate dicts
authorD = {}	#{'author' : {'experiment setting' : [success rates of all experiments using this exp setting]}*}
sRate = 0
with open(path) as file:
	expL = file.read().split('\n')

if expL[-1] == '':
	del expL[-1]
for exp in expL[1:]:
	cellL = exp.split(',')
	author = cellL[0]
	sRate = float(cellL[sRateIndex])
	if author not in authorD:
		authorD[author] = {}
	for i in range(1,5):
		cell = cellL[i]
		if cell not in authorD[author]:
			authorD[author][cell] = [sRate]
		else:
			authorD[author][cell].append(sRate)
		
for author, settingD in authorD.items():
	for settingName, rateL in settingD.items():
		authorD[author][settingName] = reduce(rateL)


#for a given exp setting, find average between all authors
authorL=[]
for author in authorD:
	authorL.append(author)

for setting in authorD[author]:
	total=0
	for author in authorL:
		total += authorD[author][setting][1]
	avg = total/len(authorL)
	for author in authorL:
		authorD[author][setting].append(round(avg, 6))
		


#final output
with open(dest, 'w') as file:
	file.write("True Author,Experiment Setting,Experiment Count, Avg. Success Rate, Std. Deviation, Median Success Rate, Avg Success Rate Across Authors\n") 
	for author, settingD in authorD.items():
		for setting, valueL in settingD.items():
			file.write(author + ',')
			file.write(setting)
			for value in valueL:
				file.write(','+str(value))
			file.write('\n')
		









