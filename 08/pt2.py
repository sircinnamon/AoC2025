import math
from collections import deque

filename = "input.txt"
# filename = "example.txt"

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
_min = (9999999999, (0,0,0), (0,0,0))
for i, b in enumerate(boxes):
	if(b not in distances): distances[b] = {}
	for b2 in boxes[i+1:]:
		if(b2 not in distances): distances[b2] = {}
		d = dist(b, b2)
		# print(b, b2, d)
		if(d < _min[0]): _min = (d, b, b2)
		distances[b][b2] = d
		distances[b2][b] = d

circuits = list()
circuits.append(set([_min[1], _min[2]]))
del distances[_min[1]][_min[2]]
del distances[_min[2]][_min[1]]
while(len(circuits[0]) < len(distances.keys())):
	next_join = (9999999999, (0,0,0), (0,0,0))
	for box in distances:
		for pair_box in distances[box]:
			if distances[box][pair_box] < next_join[0]:
				next_join = (distances[box][pair_box], box, pair_box)
	b1 = next_join[1]
	b2 = next_join[2]
	# print(next_join)
	# print("MAIN CIRCUIT: {} - TOTAL CIRCUITS {}".format(len(circuits[0]), len(circuits)))
	del distances[b1][b2]
	del distances[b2][b1]
	existing = False
	for c in circuits:
		if(b1 in c):
			existing = True
			c.add(b2)
			for bx in c:
				if(b1 in distances[bx]): del distances[bx][b1]
				if(bx in distances[b1]): del distances[b1][bx]
		if(b2 in c):
			existing = True
			c.add(b1)
			for bx in c:
				if(b2 in distances[bx]):del distances[bx][b2]
				if(bx in distances[b2]):del distances[b2][bx]
	if not existing:
		circuits.append(set([b1, b2]))
	# reduce overlapping circuits
	for i, c in enumerate(circuits):
		for c2 in circuits[i+1:]:
			if len(c.intersection(c2)) > 0:
				circuits[i] = c.union(c2)
				circuits.remove(c2)
# print(circuits)
# print(len(circuits[0]))
print(next_join[1][0] * next_join[2][0])
