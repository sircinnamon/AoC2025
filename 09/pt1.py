filename = "input.txt"
# filename = "example.txt"

tiles = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		tile = list(map(int, line.split(',')))
		tiles.append((tile[0], tile[1]))
		line = f.readline().strip()

mx = (0, (0,0), (0,0))
for i, t1 in enumerate(tiles):
	for j, t2 in enumerate(tiles[i+1:]):
		a = (abs(t1[0]-t2[0])+1)*(abs(t1[1]-t2[1])+1)
		# print(a, t1, t2)
		if(a > mx[0]):
			mx = (a, t1, t2)
print(mx[0])