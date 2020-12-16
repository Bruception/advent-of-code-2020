import re
import sys

class Ticket:
    def __init__(self, row):
        self.values = [int(num) for num in row.split(',')]
        self.mappings = [set() for num in self.values]

    def determineMappings(self, fields):
        for i, value in enumerate(self.values):
            for field in fields:
                for low, high in field['ranges']:
                    if (value >= low and value <= high):
                        self.mappings[i].add(field['label'])

    def isValid(self, fields):
        total = 0
        for value in self.values:
            matched = False
            for field in fields:
                for low, high in field['ranges']:
                    if (value >= low and value <= high):
                        matched = True
                        break
            if (not matched):
                return False
        return True    

def parseFields(file):
    def parseRange(range):
        low, high = range.split('-')
        return (int(low), int(high))
    fieldPattern = re.compile(r'([a-z\s]+): ([0-9]+\-[0-9]+) or ([0-9]+\-[0-9]+)')
    line = file.readline()
    fields = []
    while (line != '\n'):
        name, range1, range2 = fieldPattern.match(line).groups()
        fieldShape = {
            'label': name,
            'ranges': [parseRange(range1), parseRange(range2)],
        }
        fields.append(fieldShape)
        line = file.readline()
    return fields

def parseYourTicket(file):
    file.readline()
    line = file.readline()
    file.readline()
    return Ticket(line)

def parseNearbyTickets(file):
    file.readline()
    tickets = []
    line = file.readline()
    while (line != ''):
        tickets.append(Ticket(line))
        line = file.readline()
    return tickets

def getField(tickets):
    field = None
    for i in range(len(tickets[0].mappings)):
        intersection = set(tickets[0].mappings[i])
        for ticket in tickets:
            intersection &= ticket.mappings[i]
        if (len(intersection) == 1):
            field = intersection.pop()
            break
    return (field, i)

def determineOrdering(tickets, fields):
    fieldMappings = {field['label']: 0 for field in fields}
    for i in range(len(fields)):
        field, order = getField(tickets)
        fieldMappings[field] = order
        for ticket in tickets:
            for mapping in ticket.mappings:
                if (field in mapping):
                    mapping.remove(field)
    return fieldMappings

def parse(file):
    fields = parseFields(file)
    ticket = parseYourTicket(file)
    tickets = parseNearbyTickets(file)
    validTickets = list(filter(lambda ticket: ticket.isValid(fields), tickets))
    for t in validTickets:
        t.determineMappings(fields)
    ordering = determineOrdering(validTickets, fields)
    mul = 1
    for field in fields:
        if (re.match(r'^departure', field['label'])):
            mul *= ticket.values[ordering[field['label']]]
    print(mul)

file = open(f'{sys.path[0]}/input.txt', 'r')
parse(file)
