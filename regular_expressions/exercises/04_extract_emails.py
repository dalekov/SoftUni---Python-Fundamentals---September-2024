import re

def extract_emails(line):
    regex = r"(^|\s)(?P<email>[a-zA-Z\d]+[.-_][a-zA-Z\d]@[a-zA-Z]+[-][a-zA-Z].[.a-zA-z]*[a-zA-Z])"
    matches = re.findall(regex, line)
    for match in matches:
        print(match)

line = input()

extract_emails(line)