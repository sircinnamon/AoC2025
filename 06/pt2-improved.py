import re
from functools import reduce

filename = "input.txt"
# filename = "example.txt"

lines = list()
with open(filename, "r") as f:
	line = f.readline().replace('\n','')
	while line:
		lines.append(line)
		line = f.readline().replace('\n','')

def solve(col):
	op = col[-1].strip()
	col = col[:-1]
	reducer = lambda x,y:x+y
	total = 0
	if(op == '*'):reducer = lambda x,y:x*y; total=1;

	for i in range(len(col[0])):
		v = int(''.join(list(map(lambda x: x[i], col))).strip())
		total = reducer(total, v)
	# print(total)
	return total

total = 0
currs = ['']*len(lines)
for i in range(len(lines[0])):
	char_col = list(map(lambda x: x[i], lines))
	if(len(''.join(char_col).strip())==0):
		# CHOP COLUMN
		# print(currs)
		total+=solve(currs)
		currs = ['']*len(lines)
	else:
		currs = list(map(lambda x: x[0]+x[1], zip(currs, char_col)))
total+=solve(currs)
print(total)