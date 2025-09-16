def multiplication_table(n=int(input("Enter a number\n"))):
    for i in range(0, 10):
        print(f"{i} X {n} = {i * n}", end="\n")

multiplication_table()