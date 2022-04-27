import math
arr = [3, 4, 5]


def hasperfect(arr1):
    for i in arr1:
        root = math.sqrt(i)
        if int(root + 0.5) ** 2 == i:
            ans = True
            break
        else:
            ans = False
    return ans


hasperfect(arr)
