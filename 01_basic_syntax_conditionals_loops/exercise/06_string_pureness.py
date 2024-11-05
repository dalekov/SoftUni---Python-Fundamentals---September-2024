n = int(input())

for i in range(1, n + 1):
    string = input()

    if "," not in string and "." not in string and "_" not in string:
        print(f"{string} is pure.")
    else:
        print(f"{string} is not pure!")