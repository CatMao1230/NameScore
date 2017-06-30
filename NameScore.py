import sys

def access_from_file(file):
	with open(file) as fo:
		line = fo.readline()

	score = fix_str(line)
	score.sort()

	return score

def fix_str(s):
	s = s.strip().replace('"', '')
	score = s.split(',')

	for index, element in enumerate(score):
		score[index] = filter(str.isalpha, element).upper()
	return score

def name_score(score):
	ls = []
	for index, element in enumerate(score):
		ls.append(sum([ord(x)-64 for x in element]) * (index + 1))
	return ls

if __name__ == '__main__':
	for i in name_score(access_from_file(sys.argv[1])):
		print i
