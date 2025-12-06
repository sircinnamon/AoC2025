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

ops = re.split(r'\s+', lines[-1])
lines = lines[:-1]
cols = list()
while(len(lines[0]) > 0):
	for i in range(len(lines[0])):
		allspace = True
		for line in lines:
			if i==len(line)-1:
				i+=1
				break
			if(line[i] != ' '):
				allspace = False
				break
		if(allspace):
			col = list(map(lambda x: x[0:i], lines))
			lines = list(map(lambda x: x[i+1:], lines))
			# print(col)
			cols.append(col)
			break
# print(cols)

total = 0

def build_digits(col):
	digits = ['']*len(col[0])
	for i in range(len(col)):
		for j in range(len(col[0])):
			digits[j] = digits[j]+col[i][j]
	# print(digits)
	return list(map(lambda x: int(x.strip()), digits))
# print(lines)

for i, col in enumerate(cols):
	parsed_vals = build_digits(col)
	subtotal = 0
	if(ops[i] == '+'):
		subtotal = reduce(lambda x,y: x+y, parsed_vals)
	if(ops[i] == '*'):
		subtotal = reduce(lambda x,y: x*y, parsed_vals)
	# print(col, ops[i], subtotal)
	total+=subtotal
print(total)