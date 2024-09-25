events = input().split("|")

energy = 100
coins = 100

for event in events:
    event_type, value = event.split("-")

    value = float(value)

    if event_type == "rest":
        gained_energy = min(100 - energy, value)  # Determine how much energy is gained without exceeding 100
        energy += gained_energy
        print(f"You gained {gained_energy:.0f} energy.")
        print(f"Current energy: {energy:.0f}.")

    elif event_type == "order":
        if energy >= 30:
            energy -= 30
            coins += value
            print(f"You earned {value:.0f} coins.")
        else:
            energy += 50
            print("You had to rest!")

    else:
        if coins >= value:
            coins -= value
            print(f"You bought {event_type}.")
        else:
            print(f"Closed! Cannot afford {event_type}.")
            break
else:
    print(f"Day completed!")
    print(f"Coins: {coins:.0f}")
    print(f"Energy: {energy:.0f}")
