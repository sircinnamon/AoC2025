filename = "input.txt"
# filename = "example.txt"

lines = list()
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		lines.append(line)
		line = f.readline().strip()

splitcount = 0
lines[0] = lines[0].replace('S', '|')
for i, line in enumerate(lines):
	if(i==0):continue
	prev = lines[i-1]
	while('|' in prev):
		pos = prev.index('|')
		prev = prev[:pos] + '_' + prev[pos+1:]
		if(line[pos] == '.'):
			line = line[:pos] + '|' + line[pos+1:]
		elif(line[pos] == '^'):
			splitcount+=1
			line = line[:pos-1] + '|^|' + line[pos+2:]
	lines[i] = line
# print('\n'.join(lines))
print(splitcount)