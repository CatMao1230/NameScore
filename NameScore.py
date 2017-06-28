import sys

def access_from_file(file):
	with open(file) as fo:
		line = fo.readline()
	line = line.strip().replace('"', '')
	score = line.split(',')
	score.sort()
	return score

def name_score(score):
	ls = []
	for index, element in enumerate(score):
		ls.append(sum([ord(x)-64 for x in element]) * (index + 1))
	return ls

if __name__ == '__main__':
	for i in name_score(access_from_file(sys.argv[1])):
		print i
