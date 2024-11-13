import re

line = input()
keyword = input()

words = [keyword]

exact_match = re.compile(r'\b%s\b' % '\\b|\\b'.join(words), flags=re.IGNORECASE)

print(len(exact_match.findall(line)))
