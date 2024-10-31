n = int(input())

grades = {}

for _ in range(n):
    name = input()
    grade = float(input())

    if name not in grades:
        grades[name] = []

    grades[name].append(grade)

for key, value in grades.items():
    if sum(value) / len(value) >= 4.50:
        print(f"{key} -> {sum(value) / len(value):.2f}")
