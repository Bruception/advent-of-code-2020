import re
import sys

def parseSubrules(subrules):
    subrules = subrules.strip('\n').split(' ')
    rules = []
    buffer = []
    for rule in subrules:
        if (rule != '|'):
            buffer.append(int(rule) if rule.isnumeric() else rule)
        else:
            rules.append(buffer)
            buffer = []
    rules.append(buffer)
    return rules

rule1 = re.compile(r'^(\d+): ((\d+\s?)+)+$')
rule2 = re.compile(r'^(\d+): ((\d+\s?)+ \| (\d+\s?)+)$')
rule3 = re.compile(r'^(\d+): \"([a-b]{1})\"$')

rules = {}
messages = []

file = open(f'{sys.path[0]}/input.txt', 'r')
for line in file:
    matchesSubrule = rule1.match(line) or rule2.match(line) or rule3.match(line)
    if (matchesSubrule):
        groups = matchesSubrule.groups()
        index = int(groups[0])
        subrules = parseSubrules(groups[1])
        rules[index] = subrules
    elif (len(line) != 1):
        messages.append(line.strip('\n'))

def buildRegex(currentRule, buffer):
    r = rules[currentRule]
    for i, subrules in enumerate(r):
        first = False
        for rule in subrules:
            if (rule == 'a' or rule == 'b'):
                buffer.append(rule)
                return
            buffer.append('(')
            buildRegex(rule, buffer)
            buffer.append(')')
        if (i < len(r) - 1):
            buffer.append('|')
    return buffer

value = ''.join(buildRegex(0, []))
regex = re.compile(fr'^{value}$')
count = 0
for message in messages:
    if (regex.match(message)):
        count += 1
print(count)
