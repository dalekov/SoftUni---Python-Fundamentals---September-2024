words = input().split()
target_palindrome = input()

palindromes = []
count = 0

for word in words:
    if word == word[::-1]:
        palindromes.append(word)

    if word == target_palindrome:
        count += 1

print(palindromes)
print(f"Found palindrome {count} times")