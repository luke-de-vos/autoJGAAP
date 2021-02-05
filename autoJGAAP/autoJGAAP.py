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

#check for errors in JGAAP standard output
def hasError(path):
	with open(path) as file:
		text = file.read()
		if re.search("java.io.FileNotFoundException", text) != None:
			print("Error: File not found")
			print("Ensure no file or directory names contain commas.")
			return True
		if re.search("DecodeError", text) != None:
			print("Error: Character decode error")
			return True
		if re.search("Error:", text) != None:
			print("Error: Miscellaneous")
			print("Check " + path)
			return True
	return False


#MAIN ===========================================================

JGAAP_path = ''
for name in os.listdir():
	if '.jar' == name[-4:]:
		JGAAP_path = name
if JGAAP_path == '':
	print("Error: Unable to find JGAAP.")
	print("Ensure both the JGAAP .jar file and autoJGAAP.py are in the autoJGAAP directory.")
	exit()

print("Running...")


#check OS
if platform.system() == 'Windows':
	pyCmd = 'python'
else:
	pyCmd = 'python3'


#CLEANUP
for name in ['Configuration', 'Output', 'tmp']:
	try:
		shutil.rmtree(name)
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

#check for errors in JGAAP standard output
if hasError(outputFile):
	quit()

#EXPERIMENT RESULTS PROCESSING
os.system(pyCmd + ' Scripts/print_tmp.py tmp rawResults.txt')
os.system(pyCmd + ' Scripts/refineResults.py rawResults.txt refinedResults.csv')
os.system(pyCmd + ' Scripts/getSettingPerformance.py refinedResults.csv singleSettingPerformance.csv')


#FILE ORGANIZATION
os.mkdir("Output")
for name in ["rawResults.txt", "refinedResults.csv", "singleSettingPerformance.csv", "JGAAP_status_output.txt", "tmp"]:
	try:
		shutil.move(name, "Output")
	except FileNotFoundError: 
		pass
	
if "author_error.txt" in os.listdir():		#refineResults.py writes to author_error.txt if an author or attempt is missed for any experiment
	print("Warning: Error while attempting to identify experiment author or classification attempt.")
	print("See Output/author_error.txt for details.")
	shutil.move("author_error.txt", "Output")






