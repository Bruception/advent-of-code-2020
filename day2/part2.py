import sys
import re
class PasswordField:
    def __init__(self, line):
        match = re.match(r'^([0-9]+)-([0-9]+)\s([a-z]{1}):\s([a-z]+)$', line)
        self.min = int(match.group(1))
        self.max = int(match.group(2))
        self.char = match.group(3)
        self.password = match.group(4)
        self.firstPosValid = self.password[self.min - 1] == self.char
        self.secondPosValid = self.password[self.max - 1] == self.char
        self.isValid = self.firstPosValid ^ self.secondPosValid

file=open(f'{sys.path[0]}/input.txt', 'r')
validPasswords = 0
for line in file:
    password = PasswordField(line)
    if (password.isValid):
        validPasswords += 1
print(validPasswords)
