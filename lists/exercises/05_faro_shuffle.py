cards = input().split(" ")
shuffles = int(input())

tmp_cards = list()
shuffled_cards = cards
for shuffle in range(0, shuffles):
    tmp_cards = []
    for i in range(0, int(len(shuffled_cards) / 2)):
        tmp_cards.append(shuffled_cards[i])
        tmp_cards.append(shuffled_cards[int(len(shuffled_cards) / 2) + i])

    shuffled_cards = tmp_cards

print(shuffled_cards)