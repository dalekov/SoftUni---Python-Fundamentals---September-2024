list1 = list(input())
list2 = list(input())
unique = []

# Loop over the length of the strings, transforming one character at a time
for i in range(len(list1)):
    if list1[i] != list2[i]:  # Only change the character if it's different
        list1[i] = list2[i]
        new_word = ''.join(list1)
        if new_word not in unique:  # Check if the transformation is unique
            unique.append(new_word)
            print(new_word)
