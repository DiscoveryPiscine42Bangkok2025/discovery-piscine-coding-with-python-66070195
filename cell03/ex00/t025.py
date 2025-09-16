def up_to_25(n=int(input("Enter a number less than 25\n"))):
    if n > 25:
        print("Error")
        
    for n in range(n, 26):
        print("Inside the loop, my variable is", n)

up_to_25()