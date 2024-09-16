user_input = input().split(", ")

if user_input[-1] == "wolf":
    print("Please go away and stop eating my sheep")
else:
    index_wolf = user_input.index("wolf")
    index_sheep = abs(index_wolf - (len(user_input) - 1))
    print(f"Oi! Sheep number {index_sheep}! You are about to be eaten by a wolf!")