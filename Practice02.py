fish = ["Flounder", "Sole", "Blue Cod", "Snapper", "Terakihi", "John Dory", "Red Cod"]
for i in fish:
    print(i[0])

for i in fish:
    print(i[0:3])

longest = ""
for i in fish:
    if len(i) > len(longest):
        longest = i
print(longest)

two_words = []
for i in fish:
    if " " in i:
        two_words.append(i)
print(two_words)

cod_word = []
for i in fish:
    if "Cod" in i:
        cod_word.append(i)
print(cod_word)
