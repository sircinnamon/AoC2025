import math
from collections import deque

filename = "input.txt"
# filename = "example.txt"

JUNCTION_LIMIT=1000
boxes = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		line = line.split(',')
		line = list(map(lambda x: int(x), line))
		boxes.append((line[0], line[1], line[2]))
		line = f.readline().strip()

def dist(a, b):
	return math.sqrt(
		(a[0]-b[0])**2 +
		(a[1]-b[1])**2 +
		(a[2]-b[2])**2
	)

# print(boxes)
distances = {}
connections = deque()

for i, b in enumerate(boxes):
	if(b not in distances): distances[b] = {}
	for b2 in boxes[i+1:]:
		if(b2 not in distances): distances[b2] = {}
		d = dist(b, b2)
		# print(b, b2, d)
		distances[b][b2] = d
		distances[b2][b] = d
		if(len(connections) < JUNCTION_LIMIT):
			if(len(connections) == 0):
				connections.appendleft((d, b, b2))
			else:
				i = 0
				while True:
					if i >= len(connections) or connections[i][0] < d:
						connections.insert(i, (d, b, b2))
						break
					i+=1
		elif(connections[0][0] > d):
			# print('{} smaller than {}'.format(d, connections[0][0]))
			removed = connections.popleft()
			# print('\t{} removed'.format(removed))
			inserted = False
			for i, e in enumerate(connections):
				if(e[0] < d):
					connections.insert(i, (d, b, b2))
					inserted = True
					break
			if not inserted:
				connections.append((d, b, b2))

# print(connections)

circuits = {}
while(len(connections) > 0):
	origin = connections[0][1]
	# print("=====")
	circuits[origin] = set([origin, connections[0][2]])
	q = deque([origin, connections[0][2]])
	while len(q) > 0:
		# print('Q', q)
		# print('C',circuits[origin])
		curr = q.popleft()
		for c in connections:
			# print("A", curr, c)
			if(c[1] == curr):
				# print("B1", c[2])
				q.append(c[2])
				q.append(c[1])
				circuits[origin].add(c[2])
				connections.remove(c)
				break
			elif(c[2] == curr):
				# print("B2", c[1])
				q.append(c[2])
				q.append(c[1])
				circuits[origin].add(c[1])
				connections.remove(c)
				break
# print(circuits)
sizes = (list(map(lambda x: len(x), list(circuits.values()))))
sizes.sort(reverse=True)
# print(sizes)
print(sizes[0]*sizes[1]*sizes[2])