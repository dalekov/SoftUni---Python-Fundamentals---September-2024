def next_version(x):
    if x[2] == 9:
        if x[1] == 9:
            x[0] += 1
            x[1] = 0
            x[2] = 0
        else:
            x[2] = 0
            x[1] += 1

    else:
        x[2] += 1

    return '.'.join(map(str, x))


version = list(map(int, input().split('.')))


print(next_version(version))
