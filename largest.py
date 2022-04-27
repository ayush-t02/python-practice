# WAP to find the largest number of array

import array as a

arr = a.array('i', [])
n = int(input("Enter no. of elements: "))

for i in range(n):
    arr.append(int(input()))


def largest(ele):
    ans = ele[0]

    for j in ele:
        if j > ans:
            ans = j

    return ans


print(largest(arr))
