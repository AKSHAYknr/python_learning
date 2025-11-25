nums = [5,9,1,2,4,15,6,3]
target = 13
hash_map = {}

def two_sum(nums, target):
    for i in range(0,len(nums)-1):
        if hash_map.__contains__(target - nums[i]):
            return [hash_map.get(target-nums[i]), i]
        else:
            hash_map[nums[i]] = i
    return [-1,-1]

print(two_sum(nums, 10))