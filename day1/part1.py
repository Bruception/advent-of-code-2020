import sys
file = open(f'{sys.path[0]}/input.txt', 'r')
map = {}
for line in file:
	num = int(line)
	if (num in map):
		print(num * map[num])
		break
	key = 2020 - num
	map[key] = num
