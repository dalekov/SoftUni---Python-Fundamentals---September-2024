n = int(input())

positive = []
negative = []

for i in range(1, n + 1):
    num = int(input())
    if num >= 0:
        positive.append(num)
    else:
        negative.append(num)

print(positive)
print(negative)
print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")
