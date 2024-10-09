distances = list(map(int, input().split()))
removed_elements = []

while distances:
    index = int(input())

    if index < 0:
        removed_elements = distances.pop(0)
        if distances:
            distances.insert(0, distances[-1])

    elif index >= len(distances) - 1:
        removed_element = distances.pop(-1)
        if distances:
            distances.append(distances[0])

    else:
        removed_element = distances.pop(index)


    for i in range(len(distances)):
        if distances[i] <= removed_element:
            distances[i] += removed_element
        else:
            distances[i] -= removed_element

    removed_elements.append(removed_element)


print(sum(removed_elements))