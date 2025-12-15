def move_zeros_to_end(nums):
    j = 0

    for i in range(len(nums)):
        if nums[i] != 0:
            nums[i], nums[j] = nums[j], nums[i]
            j += 1
    return nums

nums = [1, 0, 0, 3, 6, 5, 9, 0, 2, 4]
ans = move_zeros_to_end(nums)
print(ans)