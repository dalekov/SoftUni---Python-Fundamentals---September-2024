numbers = input().split()

def round_num():
    new_list = [round(float(num)) for num in numbers]

    return new_list

print(round_num())