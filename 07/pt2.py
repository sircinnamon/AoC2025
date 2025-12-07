filename = "input.txt"
# filename = "example.txt"

lines = list()
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		lines.append(line)
		line = f.readline().strip()

cache = {}
def count_timelines(route):
	if(len(route) == 1): return 1 # base case
	pos = route[0].index('|')
	if((len(route), pos) in cache):
		return cache[(len(route), pos)]
	if(route[1][pos] == '.'):
		route[1] = route[1][:pos] + '|' + route[1][pos+1:]
		count = count_timelines(route[1:])
		cache[(len(route), pos)] = count
		return count
	else:
		# split
		t_a = route[1][:pos-1] + '|' + route[1][pos:]
		t_b = route[1][:pos+1] + '|' + route[1][pos+2:]
		count = 0
		count += count_timelines([t_a]+route[2:])
		count += count_timelines([t_b]+route[2:])
		cache[(len(route), pos)] = count
		return count

lines[0] = lines[0].replace('S', '|')
# print('\n'.join(lines))
print(count_timelines(lines))
