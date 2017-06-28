import sys

def access_from_file(file):
	with open(file) as fo:
		line = fo.readline()
	line = line.strip().replace('"', '')
	score = line.split(',')
	score.sort()
	return score

def name_score(score):
	for index, element in enumerate(score):
		print sum([ord(x)-64 for x in element]) * (index + 1)

name_score(access_from_file(sys.argv[1]))
