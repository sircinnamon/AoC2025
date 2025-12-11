filename = "input.txt"
# filename = "example.txt"

graph = {}
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		line = line.split(': ')
		k = line[0]
		outs = line[1].split(' ')
		graph[k] = outs
		line = f.readline().strip()
# print(graph)

cache = {}
def count_paths(start, end, graph):
	count = 0
	if((start,end) in cache): return cache[(start,end)]
	for exit in graph[start]:
		if(exit == end): count+=1
		else:
			count += count_paths(exit, end, graph)
	# print(start, end, count)
	cache[(start,end)] = count
	return count

graph['out'] = []
ra = count_paths('svr', 'fft', graph) * count_paths('fft', 'dac', graph) * count_paths('dac', 'out', graph)
rb = count_paths('svr', 'dac', graph) * count_paths('dac', 'fft', graph) * count_paths('fft', 'out', graph)
# without loops, one of these will always be 0
# Either DAC -> FFT doesnt exist or FFT -> DAC doesnt exist
# print(ra)
# print(rb)
print(ra+rb)
# 4417740 too low