def up_low(txt=str(input())):
    for char in txt:
        if char.islower():
            print(char.upper(), end="")
        elif char.isupper():
            print(char.lower(), end="")
        else:
            print(char, end="")

up_low()
