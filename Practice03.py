sentence = str(input("Type whatever makes you happy"))
count = 0
for i in sentence:
    if i == "e":
        count += 1
print(f"You had e {count} time/s in your sentence")
