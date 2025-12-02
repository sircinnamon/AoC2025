import re

filename = "input.txt"
# filename = "example.txt"

lines = list()
dial_pos = 50
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		a = re.match(r'(.)(\d+)', line)
		val = int(a[2])
		if(a[1] == "L"):
			val = val*-1
		lines.append(val)
		line = f.readline().strip()

z_count = 0
for val in lines:
	dial_pos = (dial_pos+val+100)%100
	# print(dial_pos)
	if(dial_pos==0): z_count+=1
print(z_count)
