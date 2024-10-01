numbers = input().split()

def sort(x):
    numbers_to_int = [int(num) for num in x]
    return(sorted(numbers_to_int))

print(sort(numbers))