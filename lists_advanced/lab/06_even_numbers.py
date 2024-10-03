nums = list(map(int, input().split(", ")))

even = [i for i in range(len(nums)) if nums[i] % 2 == 0]

print(even)