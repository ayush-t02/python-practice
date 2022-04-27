import numpy as a
import math

arr = a.array([10, 20, 30])
print(arr)

arr1 = a.arange(0, 12, 2)
print(arr1)

arr2 = a.array([10, 20, 30.5, 40], float)
print(arr2)
print(arr2 + 5, arr2 - 5, arr2 * 5, arr2 / 5, arr2 % 5)

# Functions in numpy
arr3 = a.array([10, 20, 30, 40, 50])
print(math.sin(arr3))
