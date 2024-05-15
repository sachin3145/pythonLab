""" Write a Program to Display the Fibonacci Sequences up to nth Term Where n is Provided by the User. """


n = int(input("Enter upper bound of fibonacci series: "))

if n<0:
    print("Please enter a positive integer.")
    exit()
    
a, b = 0, 1
while(a<=n):
    print(a, end=" ")
    a, b = b, a+b
