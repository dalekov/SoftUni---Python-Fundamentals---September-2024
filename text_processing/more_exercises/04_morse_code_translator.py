message = input().split(' | ')

morse_code = {
    'a': ".-", 'b': "-...", 'c': "-.-.", 'd': "-..", 'e': ".", 'f': "..-.",
    'g': "--.", 'h': "....", 'i': "..", 'j': ".---", 'k': "-.-", 'l': ".-..",
    'm': "--", 'n': "-.", 'o': "---", 'p': ".--.", 'q': "--.-", 'r': ".-.",
    's': "...", 't': "-", 'u': "..-", 'v': "...-", 'w': ".--", 'x': "-..-",
    'y': "-.--", 'z': "--.."
}

decrypted_message = ''

for word in message:
    decrypted_word = ''
    letters = word.split()
    for letter in letters:
        for key, value in morse_code.items():
            if letter == value:
                decrypted_word += key.upper()
    decrypted_message += decrypted_word + ' '

print(decrypted_message)
