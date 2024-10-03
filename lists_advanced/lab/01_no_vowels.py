text = input()

no_vowels = [ch for ch in text if ch not in 'aoueiAOUEI']
print(''.join(no_vowels))