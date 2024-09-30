nums = input().split(" ")

finish_line_index = (len(nums) // 2) + 1

total_time_left = 0
total_time_right = 0

for i in range(finish_line_index - 1):
    if int(nums[i]) == 0:
        total_time_left *= 0.8
    total_time_left += int(nums[i])

for j in range(len(nums) - 1, finish_line_index - 1, -1):
    if int(nums[j]) == 0:
        total_time_right *= 0.8
    total_time_right += int(nums[j])

if total_time_right > total_time_left:
    print(f"The winner is left with total time: {total_time_left:.1f}")
else:
    print(f"The winner is right with total time: {total_time_right:.1f}")