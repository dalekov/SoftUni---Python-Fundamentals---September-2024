n = int(input())

sample_list = []

for i in range(1, n + 1):
    num = int(input())

    sample_list.append(num)

command = input().lower()

if command == "even":
    result = [num for num in sample_list if num % 2 == 0]
elif command == "odd":
    result = [num for num in sample_list if num % 2 == 1]
elif command == "negative":
    result = [num for num in sample_list if num < 0]
elif command == "positive":
    result = [num for num in sample_list if num >= 0]

print(result)
