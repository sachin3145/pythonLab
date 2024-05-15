""" Write a program of basic calculator using functions """

def add(x, y):
    return x + y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def div(x, y):
    return x / y


while True:
    print("----------------------------------CALCULATOR----------------------------------\nEnter 0: EXIT\nEnter 1: PERFORM ADDITION\nEnter 2: PERFORM SUBTRACTION\nEnter 3: PERFORM MULTIPLICATION\nEnter 4: PERFORM DIVISION")
    ch = input("Enter your choice: ")
    
    if ch == "0":
        exit()
    
    n1 = float(input("Enter 1st number: "))
    n2 = float(input("Enter 2nd number: "))
    match ch:
        case "1":
            print(f"{n1} + {n2} = {add(n1, n2)}")
        case "2":
            print(f"{n1} - {n2} = {sub(n1, n2)}")
        case "3":
            print(f"{n1} * {n2} = {mul(n1, n2)}")
        case "4":
            print(f"{n1} / {n2} = {div(n1, n2)}")
  