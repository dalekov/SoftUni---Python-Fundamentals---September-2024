strings = input().split()

while True:
    command = input().split()
    if command[0] == "3:1":
        break

    if command[0] == "merge":
        start_index = int(command[1])
        end_index = int(command[2])

        # Handle out-of-bounds for merging
        start_index = max(0, start_index)
        end_index = min(len(strings) - 1, end_index)

        # Merge the specified range of strings
        merged_string = ''.join(strings[start_index:end_index + 1])

        # Remove the merged elements from the list
        del strings[start_index:end_index + 1]

        # Insert the merged string at the start index
        strings.insert(start_index, merged_string)

    elif command[0] == "divide":
        index = int(command[1])
        partitions = int(command[2])

        # Check if index is valid and partitions is greater than 0
        if 0 <= index < len(strings) and partitions > 0:
            element = strings[index]
            part_length = len(element) // partitions  # Calculate the length of each partition
            parts = []

            # Create partitions
            for i in range(partitions):
                if i < partitions - 1:
                    parts.append(element[i * part_length:(i + 1) * part_length])
                else:
                    parts.append(element[i * part_length:])  # Last partition gets the remainder

            # Remove the original element and insert partitions
            strings.pop(index)
            strings[index:index] = parts  # Insert at the same index

# Print the final list of strings
print(' '.join(strings))
