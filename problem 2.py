# example 1
nums = [11,7,2,15]
count = 0
nums.sort()
for i in nums:
    if nums[0]<i<nums[-1]:
        count += 1
print(count)

# example 2
nums = [-3,3,3,90]
count = 0
nums.sort()
for i in nums:
    if nums[0]<i<nums[-1]:
        count += 1
print(count)