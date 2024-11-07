txt = input()

emoticons = []

for i in range(len(txt)):
    emoticon = ""
    if txt[i] == ":" and i + 1 < len(txt):
        emoticon += txt[i] + txt[i + 1]
        emoticons.append(emoticon)

for emoticon in emoticons:
    print(emoticon)
