string = input()

count_dict = {}

for ch in string:
    if ch != ' ' and ch not in count_dict:
        count_dict[ch] = 0

    if ch in count_dict:
        count_dict[ch] += 1

for key, value in count_dict.items():
    print(f'{key} -> {value}')