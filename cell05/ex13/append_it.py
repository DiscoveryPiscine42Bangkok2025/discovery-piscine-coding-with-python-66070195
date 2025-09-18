import sys
def append_it():
    if len(sys.argv) < 2:
        print("none")
        return
    for i in sys.argv[1:]:
        if i.endswith("ism"):
            continue
        print(i+"ism")
append_it()