offers = input().split(", ")
beggars = int(input())

# Initializing a list to keep track of the profit of the beggars. Each beggars begins with 0.
beggars_profit = [0] * beggars

for i in range(len(offers)):
    beggar_index = i % beggars
    beggars_profit[beggar_index] += int(offers[i])


print(beggars_profit)
