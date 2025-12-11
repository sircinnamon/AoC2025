filename = "input.txt"
# filename = "example.txt"

graph = {}
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		line = line.split(': ')
		k = line[0]
		outs = set(line[1].split(' '))
		graph[k] = outs
		line = f.readline().strip()
# print(graph)

def count_paths(start, end, graph):
	count = 0
	for exit in graph[start]:
		if(exit == end): count+=1
		else: count+=count_paths(exit, end, graph)
	return count

print(count_paths('you', 'out', graph))