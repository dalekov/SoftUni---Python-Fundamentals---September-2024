n = int(input())

parking = {}

for i in range(n):
    command = input().split()

    if command[0] == "register":
        username = command[1]
        license_plate = command[2]

        if username not in parking:
            parking[username] = license_plate
            print(f"{username} registered {license_plate} successfully")
        else:
            print(f"ERROR: already registered with plate number {parking[username]}")

    elif command[0] == "unregister":
        username = command[1]

        if username in parking:
            del parking[username]
            print(f"{username} unregistered successfully")
        else:
            print(f"ERROR: user {username} not found")

for key, value in parking.items():
    print(f"{key} => {value}")