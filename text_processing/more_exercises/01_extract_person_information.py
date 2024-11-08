import re

n = int(input())

for i in range(n):
    sentence = input()
    pattern_name = r'@\w+\|'
    pattern_age = r'#\w+\*'

    match_name = re.findall(pattern_name, sentence)
    match_age = re.findall(pattern_age, sentence)

    name = match_name[0].strip('@').strip('|')
    age = match_age[0].strip('#').strip('*')

    print(f'{name} is {age} years old.')
