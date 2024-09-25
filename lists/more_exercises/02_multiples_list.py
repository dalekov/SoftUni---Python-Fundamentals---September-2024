factor = int(input())
count = int(input())

result = []

for i in range(1, count + 1):
    num = factor * i
    result.append(num)

print(result)
