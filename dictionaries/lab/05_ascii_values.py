characters = input().split(", ")

result = {character: ord(character) for character in characters}
print(result)