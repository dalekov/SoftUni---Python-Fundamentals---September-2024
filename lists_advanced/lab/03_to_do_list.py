to_do_list = [0] * 10

while True:
    command = input().split('-')

    if command[0] == "End":
        break

    priority = int(command[0]) - 1
    action = command[1]

    to_do_list.pop(priority)
    to_do_list.insert(priority, action)

    result = [action for action in to_do_list if action != 0]

print(result)
