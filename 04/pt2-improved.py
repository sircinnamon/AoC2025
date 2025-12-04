filename = "input.txt"
# filename = "example.txt"

grid = list()
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		grid.append(list(line))
		line = f.readline().strip()

def get_adj_counts(grid):
	adj_counts = list()
	d = len(grid)
	for i in range(d):
		adj_counts.append(list([0]*d))
	for y, row in enumerate(grid):
		for x, p in enumerate(row):
			if(p=='@'):
				if x>0: adj_counts[y][x-1]+=1
				if x>0 and y>0: adj_counts[y-1][x-1]+=1
				if y>0: adj_counts[y-1][x]+=1
				if x<d-1 and y>0: adj_counts[y-1][x+1]+=1
				if x<d-1: adj_counts[y][x+1]+=1
				if x<d-1 and y<d-1: adj_counts[y+1][x+1]+=1
				if y<d-1: adj_counts[y+1][x]+=1
				if x>0 and y<d-1: adj_counts[y+1][x-1]+=1
			if(p=='.' or p=='X'):
				adj_counts[y][x] += 1000
	return adj_counts

changed = True
rounds = 0
adj_counts = get_adj_counts(grid)
while(changed):
	# print('ROUND {}'.format(rounds))

	rounds+=1
	changed = False
	d = len(adj_counts)
	for y, row in enumerate(adj_counts):
		for x, v in enumerate(row):
			if(v<4):
				changed = True
				grid[y][x] = 'X'
				adj_counts[y][x] = 9999
				if x>0: adj_counts[y][x-1]-=1
				if x>0 and y>0: adj_counts[y-1][x-1]-=1
				if y>0: adj_counts[y-1][x]-=1
				if x<d-1 and y>0: adj_counts[y-1][x+1]-=1
				if x<d-1: adj_counts[y][x+1]-=1
				if x<d-1 and y<d-1: adj_counts[y+1][x+1]-=1
				if y<d-1: adj_counts[y+1][x]-=1
				if x>0 and y<d-1: adj_counts[y+1][x-1]-=1
print(''.join(map(lambda x: ''.join(x), grid)).count('X'))