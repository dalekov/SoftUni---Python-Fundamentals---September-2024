def exchange(lst, index):
    if 0 <= index < len(lst):
        return lst[index + 1:] + lst[:index + 1]
    print("Invalid index")
    return lst


def find_max_min(lst, odd_even, max_min):
    filtered = [num for num in lst if num % 2 == (0 if odd_even == "even" else 1)]
    if not filtered:
        print("No matches")
        return
    target = max(filtered) if max_min == "max" else min(filtered)
    print(len(lst) - 1 - lst[::-1].index(target))


def get_elements(lst, count, odd_even, first_last):
    if count > len(lst):
        print("Invalid count")
        return
    filtered = [num for num in lst if num % 2 == (0 if odd_even == "even" else 1)]
    result = filtered[:count] if first_last == "first" else filtered[-count:]
    print(result)


def main():
    numbers = list(map(int, input().split()))

    while True:
        command = input().split()
        action = command[0]

        if action == "end":
            print(numbers)
            break
        elif action == "exchange":
            numbers = exchange(numbers, int(command[1]))
        elif action in ["max", "min"]:
            find_max_min(numbers, command[1], action)
        elif action in ["first", "last"]:
            get_elements(numbers, int(command[1]), command[2], action)


if __name__ == "__main__":
    main()