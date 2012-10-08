#!/usr/bin/env python

import random
import re
import StringIO

# Generates pseudo-random text, dog inspired
class DoggieIpsum:
	def __init__(self):
		self.splitRegex = re.compile("([^,\\n]+)")

		self.dogsWords = self.__dogs()
		self.ipsumWords = self.__ipsum()

	# Reads the dogs file
	def __dogs(self):
		fdogs = open("dogs.csv", "r")
		
		dogsStr = fdogs.read()

		return self.splitRegex.findall(dogsStr)
	
	# Reads the ipsum file
	def __ipsum(self):
		fipsum = open("ipsum.csv", "r")
		
		ipsumStr = fipsum.read()

		return self.splitRegex.findall(ipsumStr)
	
	# Generates text, with or without ipsum
	def ipsum(self, numPara, useIpsum, commaChance):
		words = self.dogsWords
		generatedIpsum = StringIO.StringIO()

		if useIpsum:
			words.extend(self.ipsumWords)

		random.shuffle(words)

		numPara = 5 if numPara <= 0 else numPara

		for pidx in range(numPara):
			random.seed()
			numWords = random.randint(25,50)
			paragraph = StringIO.StringIO()

			for widx in range(numWords):
				random.seed()
				wordIdx = random.randint(0, len(words) - 1)

				paragraph.write(words[wordIdx])

				if widx == numWords - 1:
					paragraph.write(". ")
				else:
					# Adds a comma
					if random.randint(1, 100) <= commaChance:
						paragraph.write(",")

					paragraph.write(" ")

			if pidx < numPara - 1:
				paragraph.write("\n")
			
			paragraph.flush()
			generatedIpsum.write(paragraph.getvalue().capitalize())
			paragraph.close()
		
		generatedIpsum.flush()
		doggieIpsum = generatedIpsum.getvalue()
		generatedIpsum.close()

		return doggieIpsum
