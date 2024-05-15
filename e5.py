""" write a program to create a list and swap two items of a list """

myList = []

l = int(input("Enter the number of elements to add in list: "))

for i in range(l):
    myList.append(int(input(f"Enter number to be entered at index {i}: ")))

print("\nList before swapping: ", myList)

i , j = map(int, input("\nEnter indices to be swapped: ").split(" "))

myList[i], myList[j] = myList[j], myList[i]

print("List after swapping: ", myList)