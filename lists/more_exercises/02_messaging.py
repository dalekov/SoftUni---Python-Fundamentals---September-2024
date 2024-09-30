nums = input().split(" ")
string = input()

message = ""

for el in nums:
    total = 0
    for ch in el:
        total += int(ch)

    # If the index, exceeds the list length, we wrap around from the beginning.
    index = total % len(string)

    new_ch = string[index]
    message += new_ch
    string = string.replace(string[index], '', 1)

print(message)