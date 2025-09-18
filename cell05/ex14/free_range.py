import sys
def free_range(start, end):
    start, end = int(start), int(end)
    if start >= end:
        start, end = end, start
    return list(range(start, end+1))
if len(sys.argv) == 3: print(free_range(sys.argv[1], sys.argv[2])) 
else: print("none")