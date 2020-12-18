import sys
import heapq

class ExpressionNode:
    def __init__(self, value, index, level):
        self.index = index
        self.value = value
        self.level = level
        self.isOperand = (value == '+' or value == '*')
        self.left = None
        self.right = None
    
    def evaluate(self):
        if (not self.isOperand):
            return int(self.value)
        if (self.value == '+'):
            return self.left.evaluate() + self.right.evaluate()
        return self.left.evaluate() * self.right.evaluate()

    def __lt__(self, other):
        if (self.level == other.level):
            return not (self.value < other.value)
        return self.level < other.level

    def __repr__(self):
        return str(self.value)

file = open(f'{sys.path[0]}/input.txt', 'r')
lines = [list(filter(None, list(line.strip('\n').replace(' ', '')))) for line in file]

def evaluateLine(line): 
    leftMost, rightMost = {}, {}
    expressions, operands = [], []
    level, index = 0, 0
    for token in line:
        if (token == '(' or token == ')'):
            level += -1 if token == '(' else 1
            continue
        expression = ExpressionNode(token, index, level)
        expressions.append(expression)
        leftMost[expression] = index
        rightMost[expression] = index
        if (expression.isOperand):
            heapq.heappush(operands, expression)
        index += 1
    current, left, right = None, 0, 0
    while (operands):
        current = heapq.heappop(operands)
        left = leftMost[expressions[current.index - 1]]
        right = rightMost[expressions[current.index + 1]]
        current.left = expressions[left]
        current.right = expressions[right]
        expressions[left], expressions[right] = current, current
        leftMost[current] = left
        rightMost[current] = right
    return current.evaluate()

print(sum(evaluateLine(line) for line in lines))
