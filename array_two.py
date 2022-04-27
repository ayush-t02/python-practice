# WAP for storing students marks, find total and average

import array as a

arr = a.array('i', [])
n = int(input("Number of students: "))
print("Enter the marks: ")
for i in range(n):
    arr.append(int(input()))


def results(marks):
    s = sum(arr)
    avg = s / len(arr)
    print(s)
    print(avg)


results(arr)
