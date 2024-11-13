import re

lines = []

while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break

text = '\n'.join(lines)

regex = r'[0-9]+'

matches = re.findall(regex, text)

for match in matches:
    print(match, end=" ")

