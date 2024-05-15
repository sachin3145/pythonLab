""" Create a list and use map, reduce and filter on it """

from functools import reduce

myList  = [1, 2, 3, 4, 5, 6, 7]

# implementation of maps

mappedList = list(map(lambda x: x**2, myList)) 
print(mappedList)

# implementation of filter

filteredList = list(filter(lambda x: x%2==0, myList))
print(filteredList)

# implementation of reduce

reducedValue = reduce(lambda x, y: x*y, myList)
print(reducedValue)