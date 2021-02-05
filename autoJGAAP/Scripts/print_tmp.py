

import os
import sys

tmpPath = sys.argv[1]
dest = sys.argv[2]

for path, subdirs, files in os.walk(tmpPath):
	for name in files:
		with open(os.path.join(path, name)) as file:
			with open(dest, 'a') as destFile:
				text = file.read()
				destFile.write(text)
