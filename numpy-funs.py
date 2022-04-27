import numpy
from numpy import *

arr3 = numpy.array([10, 20, 30, 40, 50])

for i in arr3:
    print(sin(i), cos(i), tan(i))

print(sum(arr3), min(arr3), max(arr3), mean(arr3), median(arr3))
