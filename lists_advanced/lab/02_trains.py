n = int(input())

train = [0] * n

while True:
    command = input().split()

    if command[0] == 'End':
        break

    if command[0] == 'add':
        train[-1] += int(command[1])

    if command[0] == 'insert':
        train[int(command[1])] += int(command[2])

    if command[0] == 'leave':
        train[int(command[1])] -= int(command[2])

print(train)