n = int(input())

def tribonacci(x):
    sequence_list = []
    for i in range(1, x + 1):
        if (i == 1) or (i == 2):
            sequence_list.append(1)
        elif (i == 3):
            sequence_list.append(2)
        else:
            new_value = sequence_list[-1] + sequence_list[-2] + sequence_list[-3]
            sequence_list.append(new_value)


    return ' '.join(map(str, sequence_list))

print(tribonacci(n))