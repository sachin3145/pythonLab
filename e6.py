""" write a program to create a dictionary, check the presence of a key in dictionary and print the sum of all values in dictionary """

myDict = {"A":1, "B":2, "C":3, "D":4, "E":5}

query = input("Enter key to find: ")

if query in myDict.keys():
    print(f"Value corresponding to key \"{query}\" is {myDict[query]}")
else:
    print(f"Key \"{query}\" does not exists")


print("\nDictionary: ", myDict)
print(f"Sum of all values of dictionary is {sum(myDict.values())}")