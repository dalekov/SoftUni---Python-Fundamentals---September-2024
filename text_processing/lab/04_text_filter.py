banned_strings = input().split(", ")
text = input()

for banned_string in banned_strings:
    if banned_string in text:
        text = text.replace(banned_string, "*" * len(banned_string))

print(text)