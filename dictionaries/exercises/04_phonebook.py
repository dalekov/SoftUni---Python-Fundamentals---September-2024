phonebook = {}


while True:
    command = input().split('-')

    if command[0].isdigit():
        for i in range(int(command[0])):
            search_name = input()
            if search_name in phonebook:
                print(f"{search_name} -> {phonebook[search_name]}")
            else:
                print(f"Contact {search_name} does not exist.")
        break

    phonebook[command[0]] = command[1]



