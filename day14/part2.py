import re
import sys

def branch(mask, address, addresses, buffer, current = 0):
    if (current == 36):
        addresses.append(''.join(buffer))
        return
    bit = mask[current]
    if (bit != 'X'):
        buffer.append(address[current] if bit == '0' else '1')
        branch(mask, address, addresses, buffer, current + 1)
    else:
        bufferCopy = buffer.copy()
        buffer.append('0')
        branch(mask, address, addresses, buffer, current + 1)
        bufferCopy.append('1')
        branch(mask, address, addresses, bufferCopy, current + 1)
    return addresses

file = open(f'{sys.path[0]}/input.txt', 'r')
memPattern = re.compile(r'^mem\[([0-9]+)\] = ([0-9]+)$')
mask = None
memory = {}
for line in file:
    line = line[:-1] if line[-1] == '\n' else line
    isMem = memPattern.match(line)
    if (isMem):
        address, value = isMem.groups()
        value = int(value)
        address = bin(int(address))[2:].rjust(36, '0')
        addresses = branch(mask, address, [], [])
        for a in addresses: memory[a] = value
    else:
        mask = list(line[-36:])
print(sum(memory.values()))
