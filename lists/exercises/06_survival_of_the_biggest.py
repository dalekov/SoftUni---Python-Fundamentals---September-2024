numbers = input().split(" ")
n = int(input())

numbers_int = [int(num) for num in numbers]

for i in range(1, n + 1):
    numbers_int.remove(min(numbers_int))

numbers_str = (str(num) for num in numbers_int)
print(', '.join(numbers_str))
