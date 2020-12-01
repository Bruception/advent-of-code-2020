file = open('input.txt', 'r')
nums = sorted([int(line) for line in file])
for i in range(0, len(nums)):
	target = 2020 - nums[i]
	left = i + 1
	right = len(nums) - 1
	while (left < right):
		total = nums[left] + nums[right]
		if (total == target):
			print(nums[left], nums[right], nums[i])
			print(nums[left] * nums[right] * nums[i])
			break
		if (total < target):
			left += 1
		if (total > target):
			right -= 1
