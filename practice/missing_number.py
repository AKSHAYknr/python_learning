nums = [1,0,3,4]

nums.sort()

for i in range(0, len(nums)):
    if i != nums[i]:
        print(i)
        break