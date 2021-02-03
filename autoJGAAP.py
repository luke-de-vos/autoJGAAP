'''
Luke De Vos
EVL Labs
syntax:
	Windows:
		python autoJGAAP.py
	Linux:
		python3 autoJGAAP.py
'''
import re
import os
import shutil
import platform

JGAAP_path = "JGAAP-8.0.0-alpha-7.jar"

print("Running...")

#check OS
if platform.system() == 'Windows':
	pyCmd = 'python'
else:
	pyCmd = 'python3'

#CLEANUP
rmList = ['tmp', 'Configuration', 'Results']
for dirName in rmList:
	try:
		shutil.rmtree(dirName)
	except FileNotFoundError: 
		pass


#WRITE CONFIGURATION FILES
os.mkdir('Configuration')
#corpus config
os.system(pyCmd + ' Scripts/printCorpusConfig.py Documents Configuration/corpusConfig.csv')
#settings config
os.system(pyCmd + ' Scripts/printSettingsConfig.py settings.csv Configuration/settingsConfig.csv')


#RUN EXPERIMENTS
outputFile = 'JGAAP_status_output.txt'
os.system('java -jar ' + JGAAP_path + ' -ee Configuration/settingsConfig.csv > ' + outputFile)
#ensure JGAAP found all documents
with open(outputFile) as file:
	text = file.read()
	searchObj = re.search("java.io.FileNotFoundException", text)
	if searchObj != None:
		print("Error: File not found")
		print("Ensure no file or directory names contain commas")
		shutil.rmtree('Configuration')
		quit() 
	searchObj = re.search("DecodeError", text)
	if searchObj != None:
		print("Error: Character decode error")
		shutil.rmtree('Configuration')
		quit() 


#RESULTS PROCESSING
os.mkdir('Results')
os.system(pyCmd + ' Scripts/print_tmp.py tmp rawResults.txt')
os.system(pyCmd + ' Scripts/refineResults.py rawResults.txt refinedResults.csv')
os.system(pyCmd + ' Scripts/getSettingPerformance.py refinedResults.csv singleSettingPerformance.csv')

shutil.move("rawResults.txt", "Results")
shutil.move("refinedResults.csv", "Results")
shutil.move("singleSettingPerformance.csv", "Results")






