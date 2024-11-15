import re

racers = input().split(", ")
results = {}

while True:
    command = input()
    if command == "end of race":
        top_3 = sorted(results.items(), key=lambda x: x[1], reverse=True)[:3]
        def add_ordinal_suffix(position):
            if 10 <= position % 100 <= 13:
                suffix = "th"
            else:
                suffix = {1: "st", 2: "nd", 3: "rd"}.get(position % 10, "th")
            return f"{position}{suffix}"

        for i, (name, score) in enumerate(top_3, start=1):
            position = add_ordinal_suffix(i)
            print(f"{position} place: {name}")
        break

    regex_digits = r'\d'
    regex_name = r'[a-zA-Z]'

    digits = re.findall(regex_digits, command)
    name = ''.join(re.findall(regex_name, command))
    distance = sum(int(digit) for digit in digits)

    if name in racers:
        if name in results:
            results[name] += distance
        else:
            results[name] = distance
