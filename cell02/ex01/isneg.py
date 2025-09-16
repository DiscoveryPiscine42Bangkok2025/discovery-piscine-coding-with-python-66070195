def is_negative(n):
    if n < 0:
        print("This number is negative.")
    elif n == 0:
        print("This number is both positive and negative.")
    else:
        print("This number is positive.")

is_negative(int(input()))