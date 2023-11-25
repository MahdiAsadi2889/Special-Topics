nums = [7, 2, 1, 10, 3]
n = len(nums)
for i in range(n-1):
    for j in range(n-1-i):
        if nums[j] > nums[j + 1]:
            nums[j], nums[j + 1] = nums[j + 1], nums[j]
print(nums)
