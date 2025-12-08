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
distances = list()
for i, b in enumerate(boxes):
	for b2 in boxes[i+1:]:
		d = dist(b, b2)
		distances.append((d, b, b2))

distances.sort()
distances = deque(distances)
circuits = list()
circuits.append(set([distances[0][1], distances[0][2]]))
distances.popleft()
while(len(circuits[0]) < len(boxes)):
	next_join = distances.popleft()
	b1 = next_join[1]
	b2 = next_join[2]
	# print(next_join)
	# print("MAIN CIRCUIT: {} - TOTAL CIRCUITS {}".format(len(circuits[0]), len(circuits)))
	existing = False
	for c in circuits:
		if(b1 in c):
			existing = True
			c.add(b2)
		if(b2 in c):
			existing = True
			c.add(b1)
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
