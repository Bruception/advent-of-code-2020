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
target = 0
for i in range(25, len(nums)):
    found = twoSum(nums, low, high, nums[i])
    if (not found):
        target = nums[i]
        break
    low += 1
    high += 1

runningSum = 0
prefixSums = {}
for i in range(len(nums)):
    runningSum += nums[i]
    prefixSums[runningSum] = i
    key = runningSum - target
    if (key in prefixSums):
        low = prefixSums[key] + 1
        high = i
        break
subarray = nums[low:high+1]
print(min(subarray) + max(subarray))
