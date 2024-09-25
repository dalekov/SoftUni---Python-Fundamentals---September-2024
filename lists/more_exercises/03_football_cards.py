A = [str(num) for num in range(1, 12)]
B = [str(num) for num in range(1, 12)]

cards = input().split(" ")

while len(cards) > 0:
    for card in cards:
        team, player_number = card.split('-')

        if team == "A" and player_number in A:
            A.remove(player_number)
        elif team == "B" and player_number in B:
            B.remove(player_number)

        cards.remove(card)

    if len(A) < 7 or len(B) < 7:
        print(f"Team A - {len(A)}; Team B - {len(B)}")
        print("Game was terminated")
        break

else:
    print(f"Team A - {len(A)}; Team B - {len(B)}")
    