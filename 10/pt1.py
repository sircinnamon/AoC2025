import re
from collections import deque
filename = "input.txt"
# filename = "example.txt"

machines = list()
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		lights = re.match(r'\[([.#]+)\]', line)
		lights = lights[1]
		buttons = re.findall(r'\(([\d,]+)\)', line)
		buttons = list(map(lambda x: [int(y) for y in x.split(',')], buttons))
		line = f.readline().strip()
		machines.append((lights, buttons))

def solve_machine(state, changes):
	known_states = set([state])
	q = deque([(state, 0)])
	while len(q) > 0:
		#BFS
		curr, curr_depth = q.popleft()
		# print(curr, curr_depth)
		if('#' not in curr): return curr_depth
		for c in changes:
			nxt = [(x=='#') for x in curr]
			for i in c: nxt[i] = not nxt[i]
			nxt = ''.join(["#" if x else "." for x in nxt])
			if(nxt not in known_states):
				# print(c, ' -> ', nxt)
				known_states.add(nxt)
				q.append((nxt, curr_depth+1))
	return None

total = 0
for m in machines:
	s = solve_machine(m[0], m[1])
	total+=s
print(total)
