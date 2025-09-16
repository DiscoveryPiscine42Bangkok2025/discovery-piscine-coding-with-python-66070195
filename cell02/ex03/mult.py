def multiply(a, b):
    result = a * b
    print(a, "X", b, "=", result)
    if result < 0:
        print("The result is negative.")
    elif result == 0:
        print("The result is positive and negative.")
    else:
        print("The result is positive.")

multiply(int(input("Enter the first number:\n")), int(input("Enter the second number:\n")))