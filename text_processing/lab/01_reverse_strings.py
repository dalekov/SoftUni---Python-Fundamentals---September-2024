while True:
    string = input()
    if string == "end":
        break

    reversed_string = string[::-1]

    print(f"{string} = {reversed_string}")