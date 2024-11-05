coffee = 0
commands_lower = "dogcatcodingmovie"
commands_upper = "DOGCATCODINGMOVIE"
while True:
    command = input()

    if command == "END":
        if coffee > 5:
            print("You need extra sleep")
        else:
            print(coffee)
        break
    if command in commands_lower:
        coffee += 1
    elif command in commands_upper:
        coffee += 2
