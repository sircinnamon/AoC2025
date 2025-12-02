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
	for i in range(1, (len(n)//2)+1):
		# take i digits
		if(len(n)%i != 0):
			continue
		substr = n[:i]
		if(n == substr*(len(n)//i)): return True
	return False

total = 0
for r in ranges:
	# print("{} - {}".format(r[0], r[1]))
	for i in range(r[0], r[1]+1):
		if(badId(i)):
			# print('\t',i)
			total+=i
print(total)