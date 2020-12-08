import sys

def prepareInstruction(instruction):
    opcode, value = instruction.split(' ')
    return (opcode, int(value))

file = open(f'{sys.path[0]}/input.txt', 'r')
instructions = [line[:-1] if line[-1] == '\n' else line for line in file]
instructions = list(map(prepareInstruction, instructions))

visited = {}
accumulator = 0
instructionCount = len(instructions)
currentInstruction = 0
while (currentInstruction < instructionCount):
    if (currentInstruction in visited):
        break
    visited[currentInstruction] = True
    opcode, offset = instructions[currentInstruction]
    if (opcode == 'acc'):
        accumulator += offset
        currentInstruction += 1
    elif (opcode == 'jmp'):
        currentInstruction += offset
    elif (opcode == 'nop'):
        currentInstruction += 1

print(accumulator)
