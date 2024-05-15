""" write a numpy program to  a) create 1d array b) 2d array c) matrix multiplication d) horizontal and vertical stacking of arrays """

import numpy as np

npArr1D = np.array([1, 2])
print(f"{npArr1D} is a {npArr1D.ndim} dimensional array")

npArr2D = np.array([[1, 2],[1, 2]])
print(f"{npArr2D} is a {npArr2D.ndim} dimensional array")

mulRes = np.matmul(npArr1D, npArr2D)
print(f"Matrix multiplication of {npArr1D} and {npArr2D} gives {mulRes}")

inputArr1 = np.array([0, 1, 2, 3, 4])
inputArr2 = np.array([5, 6, 7, 8, 9])

hStackArr = np.hstack((inputArr1, inputArr2))
print(f"Horizontal stacking of {inputArr1} and {inputArr2} gives: {hStackArr}")

vStackArr = np.vstack((inputArr1, inputArr2))
print(f"Vertical stacking of {inputArr1} and {inputArr2} gives:\n{vStackArr}")
