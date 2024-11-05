while True:
    command = input()
    output = ''
    if command == "SoftUni":
        continue
    elif command == "End":
        break

    for ch in command:
        output += ch + ch

    print(output)