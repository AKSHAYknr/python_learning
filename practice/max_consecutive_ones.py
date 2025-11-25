nums = [1,0,1,0,1,0,1,0,1,0]

max_ones = 0
count = 0
current_max = 0

for num in nums:
    if num == 1:
        count += 1
    else:
        current_max = count
        count = 0
    max_ones = max(max_ones, current_max)

print(max_ones)