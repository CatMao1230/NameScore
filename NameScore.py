# "CDEF","ABC","FIJK"

Score = []
with open("NameScore.dat") as fo:
	line = fo.readline()

line = line[:-1].replace('"', '')
Score = line.split(',')
Score.sort()
for i in range(len(Score)):
	sum = 0
	for j in range(len(Score[i])):
		sum += ord(Score[i][j]) - 64
	print sum * (i + 1)
