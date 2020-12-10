import re
import sys

class Passport:
    def __init__(self):
        self.fields = []

    def addField(self, field):
        self.fields.append(field)

    def isValid(self):
        passportLine = ' '.join(self.fields)
        fields = passportLine.split(' ')
        necessaryFields = list(filter(lambda field: field[0:3] != 'cid', fields))
        return len(necessaryFields) == 7

passports = []
passport = Passport()
file = open(f'{sys.path[0]}/input.txt', 'r')
for line in file:
    if (line != '\n'):
        passport.addField(line[0:-1])
        continue
    passports.append(passport)
    passport = Passport()
passports.append(passport)

valid = 0
for passport in passports:
    if (passport.isValid()):
        valid += 1
print(valid)
