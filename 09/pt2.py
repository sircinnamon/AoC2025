filename = "input.txt"
# filename = "example.txt"

tiles = []
edges = []
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		tile = list(map(int, line.split(',')))

		tiles.append((tile[0], tile[1]))
		line = f.readline().strip()

# arrange edges to always go Left->Rright, Top->Bottom
for i, t in enumerate(tiles):
	t1, t2 = tiles[i-1], t
	if(t1[0] > t2[0]):
		t1, t2 = t2, t1
	if(t1[1] > t2[1]):
		t1, t2 = t2, t1
	edges.append((t1,t2))

# print(edges)
pip_cache = {}
def pip(poly, p):
	if(p in pip_cache):
		return pip_cache[p]
	draw_line = ((-1,p[1]), (p[0], p[1]))
	in_poly = (list(map(lambda x: edges_cross(x, draw_line), poly)).count(True) % 2 == 1)
	pip_cache[p] = in_poly
	return in_poly

def edges_cross(edge1, edge2):
	# print(edge1, edge2)
	if(edge1[0][1] == edge1[1][1] and edge2[0][1] == edge2[1][1]):
		# both horizontal and parallel, cannot cross
		return False
	if(edge1[0][0] == edge1[1][0] and edge2[0][0] == edge2[1][0]):
		# both vertical and parallel, cannot cross
		return False
	vert = edge1
	horiz = edge2
	if(vert[0][0] != vert[1][0]):
		vert, horiz = horiz, vert
	return (
		vert[0][0] > horiz[0][0] and vert[0][0] < horiz[1][0] and
		horiz[0][1] > vert[0][1] and horiz[0][1] < vert[1][1]
	)

def polys_cross(poly1, poly2):
	for edge1 in poly1:
		for edge2 in poly2:
			if(edges_cross(edge1, edge2)):
				return True
	return False

mx = (0, (0,0), (0,0))
for i, t1 in enumerate(tiles):
	# print("{} {}".format(i, t1))
	for j, t2 in enumerate(tiles[i+1:]):
		# print("{}:{} {}".format(i,j, t2))
		a = (abs(t1[0]-t2[0])+1)*(abs(t1[1]-t2[1])+1)
		mt1 = t1
		mt2 = t2
		if(a <= mx[0]):
			continue
		# shrink corners 0.5
		if(mt1[0]>=mt2[0]):
			mt1 = (mt1[0]-0.5, mt1[1])
			mt2 = (mt2[0]+0.5, mt2[1])
		else:
			mt1 = (mt1[0]+0.5, mt1[1])
			mt2 = (mt2[0]-0.5, mt2[1])
		if(mt1[1]>=mt2[1]):
			mt1 = (mt1[0], mt1[1]-0.5)
			mt2 = (mt2[0], mt2[1]+0.5)
		else:
			mt1 = (mt1[0], mt1[1]+0.5)
			mt2 = (mt2[0], mt2[1]-0.5)
		opp1 = (mt1[0], mt2[1])
		opp2 = (mt2[0], mt1[1])
		if(pip(edges, opp1) and pip(edges, opp2)):
			r_edges = [
				(mt1, opp1),
				(opp1, mt2),
				(mt2, opp2),
				(opp2, mt1)
			]
			for i, e in enumerate(r_edges):
				p1, p2 = e[0], e[1]
				if(p1[0] > p2[0]):
					p1, p2 = p2, p1
				if(p1[1] > p2[1]):
					p1, p2 = p2, p1
				r_edges[i] = (p1, p2)
			if not polys_cross(r_edges, edges):
				# print("New record: {} {}x{}".format(a, t1, t2))
				mx = (a, t1, t2)
# print(mx)
print(mx[0])
# 4623743592 too high