#Luke De Vos

import os
import sys

corpus = sys.argv[1]
dest = sys.argv[2]

with open(dest, 'w') as file:
	for directory in os.listdir(corpus):
		for author in os.listdir(corpus + '/' + directory): 
			for song in os.listdir(corpus + '/' + directory + '/' + author):
				if directory == "Known":
					file.write(author)
				file.write(',')
				file.write(corpus + '/' + directory + '/' + author + '/' + song + ',')
				file.write(song + " by " + author)
				file.write('\n')


