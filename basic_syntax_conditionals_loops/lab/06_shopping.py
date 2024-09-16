budget = int(input())

while True:
    command = input()

    if command == "End":
        if budget >= 0:
            print("You bought everything needed.")
        break

    if budget >= int(command):
        budget -= int(command)
    else:
        print("You went in overdraft!")
        break
