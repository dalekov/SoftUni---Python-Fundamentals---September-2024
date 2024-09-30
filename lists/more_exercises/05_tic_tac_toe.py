first_row = input().split()
second_row = input().split()
third_row = input().split()

# Three down - left, middle, right
# Left
if first_row[0] == second_row[0] == third_row[0] != '0':
    if first_row[0] == "1":
        print("First player won")
    elif first_row[0] == "2":
        print("Second player won")

# Mid1dle
elif first_row[1] == second_row[1] == third_row[1] != '0':
    if first_row[1] == "1":
        print("First player won")
    elif first_row[1] == "2":
        print("Second player won")

# Right
elif first_row[2] == second_row[2] == third_row[2] != '0':
    if first_row[2] == "1":
        print("First player won")
    elif first_row[2] == "2":
        print("Second player won")

# Three across - up, middle, down
# Up
elif first_row[0] == first_row[1] == first_row[2] != '0':
    if first_row[0] == "1":
        print("First player won")
    elif first_row[0] == "2":
        print("Second player won")

# Middle
elif second_row[0] == second_row[1] == second_row[2] != '0':
    if second_row[0] == "1":
        print("First player won")
    elif second_row[0] == "2":
        print("Second player won")

# Down
elif third_row[0] == third_row[1] == third_row[2] != '0':
    if third_row[0] == "1":
        print("First player won")
    elif third_row[0] == "2":
        print("Second player won")

# Diagonal - 0, 1, 2
elif first_row[0] == second_row[1] == third_row[2] != '0':
    if first_row[0] == "1":
        print("First player won")
    elif first_row[0] == "2":
        print("Second player won")

# Diagonal - 2, 1, 0
elif first_row[2] == second_row[1] == third_row[0] != '0':
    if first_row[2] == "1":
        print("First player won")
    elif first_row[2] == "2":
        print("Second player won")

# Else - draw
else:
    print("Draw!")