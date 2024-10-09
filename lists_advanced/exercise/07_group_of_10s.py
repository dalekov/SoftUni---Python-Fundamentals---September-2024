numbers = list(map(int, input().split(", ")))

max_value = 0
while numbers:
    max_value += 10
    output = []

    for num in numbers[:]: # Iterate over a copy of numbers to avoid modifying the list while iterating
        if num <= max_value:
            output.append(num)
            numbers.remove(num)


    print(f"Group of {max_value}'s: {output}")

