def calculator(a, b):
    print("Thank  you!")
    print(a, "+", b, "=", a + b)
    print(a, "-", b, "=", a - b)
    if b != 0:
        print(a, "/", b, "=", a / b)
    else:
        print("Division by 0 is not allowed.")
    print(a, "*", b, "=", a * b)

calculator(int(input("Enter the first number: ")), int(input("Enter the second number: ")))
