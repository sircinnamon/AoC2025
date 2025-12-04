filename = "input.txt"
# filename = "example.txt"

adj_counts = list()
with open(filename, "r") as f:
	line = f.readline().strip()
	y = 0
	d = len(line)
	for i in range(d):
		adj_counts.append(list([0]*d))
	while line:
		for x, p in enumerate(line):
			if(p=='@'):
				if x>0: adj_counts[y][x-1]+=1
				if x>0 and y>0: adj_counts[y-1][x-1]+=1
				if y>0: adj_counts[y-1][x]+=1
				if x<d-1 and y>0: adj_counts[y-1][x+1]+=1
				if x<d-1: adj_counts[y][x+1]+=1
				if x<d-1 and y<d-1: adj_counts[y+1][x+1]+=1
				if y<d-1: adj_counts[y+1][x]+=1
				if x>0 and y<d-1: adj_counts[y+1][x-1]+=1
			if(p=='.'):
				adj_counts[y][x] += 1000
		line = f.readline().strip()
		y+=1
# print(adj_counts)
count = 0
for y in adj_counts:
	for x in y:
		if(x<4): count+=1
print(count)