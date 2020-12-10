import sys

file = open(f'{sys.path[0]}/input.txt', 'r')
nums = sorted([int(line) for line in file])
numOnes = 1
numThrees = 1
for i in range(len(nums) - 1):
    if (nums[i] == nums[i + 1] - 1):
        numOnes += 1
    elif (nums[i] == nums[i + 1] - 3):
        numThrees += 1
print(numOnes * numThrees)
