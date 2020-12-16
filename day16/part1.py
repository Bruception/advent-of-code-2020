import re
import sys

class Ticket:
    def __init__(self, row):
        self.values = [int(num) for num in row.split(',')]

    def getError(self, fields):
        total = 0
        for value in self.values:
            matched = False
            for field in fields:
                for low, high in field['ranges']:
                    if (value >= low and value <= high):
                        matched = True
                        break
            if (not matched):
                total += value
        return total

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

def parse(file):
    fields = parseFields(file)
    ticket = parseYourTicket(file)
    tickets = parseNearbyTickets(file)
    print(sum(ticket.getError(fields) for ticket in tickets))

file = open(f'{sys.path[0]}/input.txt', 'r')
parse(file)
