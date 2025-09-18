import sys
def match_param():
    if len(sys.argv) != 2:
        print("none")
        return
    txt=str(input("What was the parameter? "))
    if txt == sys.argv[1]:
        print("Good job!")
    else:
        print("Nope, sorry...")
match_param()
