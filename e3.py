""" Write a Program to Find the Factorial of a Number. """

factorial = 1
n = int(input("Enter number to find factorial: "))

if n<0:
    print("Please enter a positive integer.")
    exit()

for i in range(n, 0, -1):
    factorial *= i

print(f"Factorial of {n} is {factorial}.")
