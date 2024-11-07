txt = input()

result = ""

for ch in txt:
    result += chr(ord(ch) + 3)

print(result)
