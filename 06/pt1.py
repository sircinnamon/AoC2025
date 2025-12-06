import re
from functools import reduce

filename = "input.txt"
# filename = "example.txt"

lines = list()
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		lines.append(re.split(r'\s+', line))
		line = f.readline().strip()

ops = lines[-1]
lines = lines[:-1]
total = 0
# print(lines)
for i in range(len(lines[0])):
	vals = list(map(lambda x: int(x[i]), lines))
	subtotal = 0
	if(ops[i] == '+'):
		subtotal = reduce(lambda x,y: x+y, vals)
	if(ops[i] == '*'):
		subtotal = reduce(lambda x,y: x*y, vals)
	total+=subtotal
print(total)