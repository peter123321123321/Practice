bread = {
         'wholemeal': 1,
         'white': 0.8,
         'cheesy white': 1.2,
         'gluten free': 1.4,}
meat = {
         'chicken': 2.7,
         'beef': 3,
         'salami': 4,
         'vegan': 3.3,}
garnish = {
         'onion': 1.7,
         'tomato': 1,
         'lettuce': 2,
         'cheese': 2.5,}

start = str(input("Welcome to the sandwhich store, are you ready to ake your sandwhich? [y/n]"))
if start == "n":
    print("Thank you")
    quit()
else:
    bread = str(input(f"What bread would you like"
                      f"{bread}"))

