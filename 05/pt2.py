filename = "input.txt"
# filename = "example.txt"

ranges = list()
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		[start, end] = line.split("-")
		ranges.append((int(start), int(end)))
		line = f.readline().strip()

# print(ranges)

u_ranges = list()
for r in ranges:
	# print(r)
	for i, ur in enumerate(u_ranges):
		# internal
		if(r[0]>= ur[0] and r[1]<=ur[1]):
			r = None
			break
		# external
		if(r[0]<=ur[0] and r[1]>=ur[1]):
			ranges.append((r[0], ur[0]-1))
			ranges.append((ur[1]+1, r[1]))
			r = None
			break
		# left overlap
		if(r[0]<ur[0] and r[1]>=ur[0]):
			r = (r[0], ur[0]-1)
		# right overlap
		if(r[0]<=ur[1] and r[1]>ur[1]):
			r = (ur[1]+1, r[1])
	if r is not None: u_ranges.append(r)
# print(u_ranges)

total = 0
for ur in u_ranges:
	total += (ur[1]-ur[0])+1
print(total)