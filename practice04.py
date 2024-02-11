sentence = str(input("Choose your sentence"))
character = str(input("Choose your character"))

count = 0
for i in sentence:
    if i == character:
        count += 1
print(f"You had {character} {count} time/s in your sentence")