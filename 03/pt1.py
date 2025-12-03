filename = "input.txt"
# filename = "example.txt"

banks = list()
with open(filename, "r") as f:
	line = f.readline().strip()
	while line:
		banks.append(list(map(lambda x: int(x), line)))
		line = f.readline().strip()

total = 0
for bank in banks:
	a = max(bank[0:-1])
	a_ind = bank.index(a)
	b = max(bank[a_ind+1:])
	total += (10*a)+b
print(total)