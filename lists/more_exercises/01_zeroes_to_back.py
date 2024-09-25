nums = input().split(", ")

nums = [int(el) for el in nums]
zeroes = [el for el in nums if el == 0]
nums = [el for el in nums if el != 0]

result = nums + zeroes
print(result)
