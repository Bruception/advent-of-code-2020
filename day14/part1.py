import re
import sys

def applyMask(mask, value):
    for i, a in enumerate(mask):
        if (a == 'X'):
            continue
        value[i] = '1' if a == '1' else '0'
    return value

file = open(f'{sys.path[0]}/input.txt', 'r')
memPattern = re.compile(r'^mem\[([0-9]+)\] = ([0-9]+)$')
mask = None
memory = {}
for line in file:
    line = line[:-1] if line[-1] == '\n' else line
    isMem = memPattern.match(line)
    if (isMem):
        address, value = isMem.groups()
        value = list(bin(int(value))[2:].rjust(36, '0'))
        memory[address] = applyMask(mask, value)
    else:
        mask = list(line[-36:])
print(sum(int(''.join(memory[address]), 2) for address in memory))
