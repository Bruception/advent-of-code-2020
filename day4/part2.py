import re
import sys

def validYear(value, min, max):
    year = int(value)
    return year >= min and year <= max

def validHeight(value):
    if (not re.search(r'^[1-9][0-9]+(cm|in)', value)):
        return False
    units = value[-2:]
    amount = int(value[:-2])
    if (units == 'cm'):
        return amount >= 150 and amount <= 193
    return amount >= 59 and amount <= 76

validationMap = {
    'byr': lambda value: validYear(value, 1920, 2002),
    'iyr': lambda value: validYear(value, 2010, 2020),
    'eyr': lambda value: validYear(value, 2020, 2030),
    'hgt': validHeight,
    'hcl': lambda value: re.search(r'^#[0-9a-f]{6}$', value),
    'ecl': lambda value: re.search(r'^amb|blu|brn|gry|grn|hzl|oth$', value),
    'pid': lambda value: re.search(r'^[0-9]{9}$', value),
}

class Passport:
    def __init__(self):
        self.fields = []

    def addField(self, field):
        self.fields.append(field)

    def isValid(self):
        passportLine = ' '.join(self.fields)
        fields = passportLine.split(' ')
        necessaryFields = list(filter(lambda field: field[0:3] != 'cid', fields))
        if (len(necessaryFields) != 7):
            return False
        for field in necessaryFields:
            prop = field[0:3]
            value = field[4:]
            if (not validationMap[prop](value)):
                return False
        return True

passports = []
passport = Passport()
file = open(f'{sys.path[0]}/input.txt', 'r')
for line in file:
    if (line != '\n'):
        passport.addField(line[0:-1] if line[-1] == '\n' else line)
        continue
    passports.append(passport)
    passport = Passport()
passports.append(passport)

valid = 0
for passport in passports:
    if (passport.isValid()):
        valid += 1
print(valid)
