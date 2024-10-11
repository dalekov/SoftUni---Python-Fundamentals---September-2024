board = input().split()

moves = 0

while True:
    command = input().split()

    if command[0] == "end":
        if board:
            print("Sorry you lose :(")
            print(' '.join(board))
        else:
            print(f"You have won in {moves} turns!")
        break

    else:
        first_index = int(command[0])
        second_index = int(command[1])

        if board:
            moves += 1
            if first_index == second_index or (first_index < 0 or first_index >= len(board)) or (second_index < 0 or second_index >= len(board)):
                el_1 = f"-{moves}a"
                el_2 = f"-{moves}a"

                middle_index = (len(board) - 1) // 2

                board.insert(middle_index + 1, el_1)
                board.insert(middle_index + 2, el_2)

                print("Invalid input! Adding additional elements to the board")
                continue

            if board[first_index] == board[second_index]:
                el_to_be_removed = board[first_index]
                board.remove(el_to_be_removed)
                board.remove(el_to_be_removed)
                print(f"Congrats! You have found matching elements - {el_to_be_removed}!")
            else:
                print("Try again!")

        else:
            continue

