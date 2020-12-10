import sys

file = open(f'{sys.path[0]}/input.txt', 'r')
nums = sorted([int(line) for line in file])
nums.insert(0, 0)

def permute(i, nums, memo = {}):
    if (i in memo):
        return memo[i]
    if (i == len(nums) - 1):
        return 1
    numWays = 0
    for j in range(i + 1, len(nums)):
        if (nums[j] - nums[i] > 3):
            break
        answer = permute(j, nums, memo)
        numWays += answer
        memo[j] = answer
    return numWays
print(permute(0, nums))
