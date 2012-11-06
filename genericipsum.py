#!/usr/bin/env python

import sys
import random
import re
import StringIO

# Generates pseudo-random text, based on two files: a generic-themed file and an ipsum file
class GenericIpsum:
	def __init__(self, genWordsFile, ipsumWordsFile):
		self.splitRegex = re.compile("([^,\\n]+)")

		self.genericWords = self.__generic(genWordsFile)
		self.ipsumWords = self.__ipsum(ipsumWordsFile)

	# Reads the dogs file
	def __generic(self, genWordsFile):
		fgeneric = open(genWordsFile, "r")
		
		genericStr = fgeneric.read()
		genericWords = self.splitRegex.findall(genericStr)
		fgeneric.close()
		
		return genericWords
	
	# Reads the ipsum file
	def __ipsum(self, ipsumWordsFile):
		fipsum = open(ipsumWordsFile, "r")
		
		ipsumStr = fipsum.read()
		ipsumWords = self.splitRegex.findall(ipsumStr)
		fipsum.close()

		return ipsumWords

	# Generates text, with or without ipsum
	def ipsum(self, numPara, useIpsum, commaChance):
		words = self.genericWords
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
		genericIpsum = generatedIpsum.getvalue()
		generatedIpsum.close()

		return genericIpsum
	
# Test method only.
if __name__ == "__main__":
	if len(sys.argv) < 3:
		print "Usage: genericipsum.py <generic_text_file> <ipsum_text_file> [<number_paragraphs> [<use_ipsum> [<comma_chance>]]]"
		sys.exit()
	
	ipsum = GenericIpsum(sys.argv[1], sys.argv[2])

	numParagraphs = 5
	useIpsum = True
	commaChance = 10

	if len(sys.argv) > 3:
		numParagraphs = int(sys.argv[3])

	if len(sys.argv) > 4:
		useIpsum = bool(sys.argv[4])

	if len(sys.argv) > 5:
		commaChance = int(sys.argv[5])

	print ipsum.ipsum(numParagraphs, useIpsum, commaChance)
