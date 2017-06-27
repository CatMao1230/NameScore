import sys

score = []
with open(sys.argv[1]) as fo:
	line = fo.readline()

line = line.strip().replace('"', '')
score = line.split(',')
score.sort()
for index, element in enumerate(score):
	sum = 0
	for j in element:
		sum += ord(j) - 64
	print sum * (index + 1)
