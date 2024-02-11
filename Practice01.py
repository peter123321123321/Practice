code = ""
while not code:
    code = str(input("Enter your 4 digit code"))
    if code == "1234":
        print("Correct!")
    else:
        print("Incorrect!")
        code = ""