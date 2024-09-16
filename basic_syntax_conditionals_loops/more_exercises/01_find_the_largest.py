number = str(int(input()))

output = ''

for i in range(len(number)):
    largest_num = max(number)
    output += largest_num
    number = number.replace(largest_num, '', 1)

print(output)