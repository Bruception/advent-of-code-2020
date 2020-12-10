import sys

file = open(f'{sys.path[0]}/input.txt', 'r')
nums = [int(line) for line in file]

def twoSum(nums, low, high, target):
    seen = {}
    for i in range(low, high + 1):
        if (nums[i] in seen):
            return True
        seen[target - nums[i]] = True
    return False

low = 0
high = 24
for i in range(25, len(nums)):
    found = twoSum(nums, low, high, nums[i])
    if (not found):
        print(nums[i])
        break
    low += 1
    high += 1
