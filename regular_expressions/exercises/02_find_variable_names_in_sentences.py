import re

line = input()

regex = r'\b_([a-zA-Z0-9]+)\b'

matches = re.findall(regex, line)

print(','.join(matches))