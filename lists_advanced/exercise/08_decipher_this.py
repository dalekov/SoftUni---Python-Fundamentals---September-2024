message = input().split()

for word in message:
    total_digits = 0
    for char in word:
        if char.isdigit():
            total_digits += 1

    if total_digits == 2:
        word = word.replace(word[:2], chr(int(word[:2])))

    elif total_digits == 3:
        word = word.replace(word[:3], chr(int(word[:3])))

    

    word = list(word)
    word[1], word[-1] = word[-1], word[1]
    print(''.join(word), end=" ")
