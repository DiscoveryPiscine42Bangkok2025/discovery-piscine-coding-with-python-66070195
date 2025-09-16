def advanced_mult():
    n=0
    while n <= 10:
        m=0
        print(f"Table de {n}: ", end="")
        while m <= 10:
            print(n*m, end=" ")
            m += 1
        n += 1
        print()

advanced_mult()