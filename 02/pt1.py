filename = "input.txt"
# filename = "example.txt"

ranges = list()
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		rs = line.split(',')
		for r in rs:
			_range = r.split('-')
			ranges.append((int(_range[0]), int(_range[1])))
		line = f.readline().strip()
# print(ranges)

def badId(n):
	n = str(n)
	if(len(n)%2 != 0): return False
	half = len(n)//2
	return n[:half] == n[half:]

total = 0
for r in ranges:
	for i in range(r[0], r[1]+1):
		if(badId(i)):
			total+=i
print(total)