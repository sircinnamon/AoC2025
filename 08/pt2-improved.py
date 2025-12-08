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

class DSU:
	# Stolen from reddit
	# This structure tracks the current circuits each box is
	# a member of. Boxes are just tracked by index and this
	# stores its current membership (self.p), and the size
	# of its self-owned circuit (self.size). size is meaningless
	# if the box is a member of a different circuit (p[x] != x)

	# num components tracks how many discrete sets exist, reduced 
	# whenever a self-owned set becomes owned by another box.
	# very clever
	def __init__(self, n):
		self.p = list(range(n))
		self.size = [1]*n
		self.n = n
		self.num_components = n

	def find(self, x):
		if(self.p[x] != x):
			self.p[x] = self.find(self.p[x])
		return self.p[x]

	def union(self, x, y):
		xr, yr = self.find(x), self.find(y)
		if xr != yr:
			if(self.size[xr] > self.size[yr]):
				xr, yr = yr, xr # larger set second
			self.p[xr] = yr
			self.size[yr] += self.size[xr]
			self.num_components-=1
			return True
		return False

# print(boxes)
edges = list()
for i, b in enumerate(boxes):
	for j, b2 in enumerate(boxes[i+1:]):
		d = dist(b, b2)
		edges.append((d, b, b2, i, j+i+1))

edges.sort()
# print(len(edges))
ds = DSU(len(boxes))
for e in edges:
	if(ds.union(e[3], e[4])):
		# print(ds.p, e[1], e[2])
		pass
	if ds.num_components == 1:
		print(e[1][0] * e[2][0])
		break
print(ds.size)