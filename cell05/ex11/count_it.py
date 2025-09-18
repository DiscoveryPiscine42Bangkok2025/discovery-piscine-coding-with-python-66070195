import sys
def count_it():
    if len(sys.argv) < 2:
        print("none")
        return
    print("parameters:", len(sys.argv)-1)
    for i in sys.argv[1:]:
        print(f"{i}: {len(i)}")
count_it()