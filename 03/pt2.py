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
	digit = 11
	index = 0
	subtotal = 0
	while digit >= 0:
		end = digit*-1
		if(end == 0): end = len(bank)
		value = max(bank[index:end])
		index += bank[index:].index(value)+1
		subtotal += (value*(10**(digit)))
		digit-=1
	# print(bank, subtotal)
	total += subtotal
print(total)