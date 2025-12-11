import re
from collections import deque
filename = "input.txt"
# filename = "example.txt"

machines = list()
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		buttons = re.findall(r'\(([\d,]+)\)', line)
		buttons = list(map(lambda x: [int(y) for y in x.split(',')], buttons))
		buttons.sort(key=lambda x: len(x), reverse=True)
		power = re.search(r'\{(.*)\}', line)
		power = [int(x) for x in power[1].split(',')]
		line = f.readline().strip()
		machines.append((tuple(power), buttons))

def solve_machine_a(state, changes):
	came_from = {}
	g_score = {}
	g_score[state] = 0
	f_score = {}
	f_score[state] = sum(state)
	q = set([state])
	while len(q) > 0:
		#A* pathfinding
		curr = None
		lowscore = 99999999
		for opt in q:
			if(f_score[opt] < lowscore):
				curr = opt
				lowscore = f_score[curr]
		q.remove(curr)
		if(-1 in curr): continue
		if(sum(curr) == 0): return g_score[curr]
		for c in changes:
			nxt = list(curr)
			nxt_gscore = g_score[curr]+1
			for i in c: nxt[i] = nxt[i]-1
			nxt = tuple(nxt)
			if(nxt not in g_score or nxt_gscore < g_score[nxt]):
				g_score[nxt] = nxt_gscore
				nxt_fscore = sum(nxt) + nxt_gscore
				f_score[nxt] = nxt_fscore
			if(nxt not in q):
				print(c, ' -> ', nxt, nxt_gscore, nxt_fscore)
				q.add(nxt)
	return None

# I tried DFS, BFS, Pathfinding... I give up
# Stolen from reddit
from z3 import *
def solve_machine_z3(state, changes, depth=0):
	# print("STATE", state)
	# print("CHANGES", changes)
	solver = Solver()
	buttons = [Int('a{}'.format(i)) for i in range(len(changes))]
	for b in buttons:
		solver.add(b >= 0)
		# print("{} >= 0".format(b))
	for i, v in enumerate(state):
		voltages = [buttons[j] for j,c in enumerate(changes) if i in c]
		solver.add(Sum(voltages) == v)
		# print("Sum({}) == {}".format(voltages, v))
	n = 0
	while solver.check() == sat:
		model = solver.model()
		n = sum([model[d].as_long() for d in model])
		solver.add(Sum(buttons) < n)
	return n

total = 0
i = 0
for m in machines:
	# print(i)
	i+=1
	s = solve_machine_z3(m[0], m[1])
	total+=s
	# print('======')
print(total)
