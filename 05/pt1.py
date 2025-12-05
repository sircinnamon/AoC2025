filename = "input.txt"
# filename = "example.txt"

ranges = list()
count = 0
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		[start, end] = line.split("-")
		ranges.append((int(start), int(end)))
		line = f.readline().strip()

	line = f.readline().strip()
	while line:
		v = int(line)
		for r in ranges:
			if(v>= r[0] and v<=r[1]):
				count+=1
				break
		line = f.readline().strip()
# print(ranges)
print(count)