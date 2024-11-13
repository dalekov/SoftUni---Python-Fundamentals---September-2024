import re
lines = []

while True:
    line = input()
    if line:
        lines.append(line)
    else:
        break


text = '\n'.join(lines)


def extract_links(string):

    regex = r'www\.[a-zA-Z0-9-]+\.[a-z]+(?:\.[a-z]+)*'

    websites = re.findall(regex, string)
    for website in websites:
        print(website)

extract_links(text)
