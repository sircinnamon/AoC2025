import re
filename = "input.txt"
# filename = "example.txt"

presents = []
present_area = []
trees = []
with open(filename, "r") as f:
	line = f.readline()
	file = ""
	while line:
		file = file + line
		line = f.readline()
	blocks = file.split('\n\n')
	trees = blocks[-1].split('\n')
	presents = [x.split('\n')[1:] for x in blocks[:-1]]
	present_area = [x.count('#') for x in blocks[:-1]]

# print(presents)
# print(present_area)
# print(trees)

count = 0
for t in trees:
	match = re.match(r'(\d+)x(\d+): ([\d ]+)', t)
	grid = (int(match.group(1)), int(match.group(2)))
	grid_area = grid[0]*grid[1]
	req_presents = [int(x) for x in match.group(3).split(' ')]
	# print(grid, req_presents)
	# print(presents[req_presents[0]])
	req_area = 0
	for i, rp in enumerate(req_presents):
		req_area += present_area[i] * rp
	# print(req_area)
	if(req_area <= grid_area):
		count += 1
print(count)