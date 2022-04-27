import array as a

arr = a.array('i', [])

n = int(input("No. of elements: "))
for i in range(n):
    arr.append(int(input()))


def sorting(ele):
    length = len(ele)
    for z in range(length - 1):
        for j in range(0, n - z - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


sorting(arr)
for i in range(len(arr)):
    print(arr[i])
