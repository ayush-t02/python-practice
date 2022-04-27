a = int(input())
b = int(input())
c = int(input())


def squares3(a1, b1, c1):
    if ((a1 ** 2 + b1 ** 2) == c1 ** 2) or ((a1 ** 2 + c1 ** 2) == b1 ** 2) or ((c1 ** 2 + b1 ** 2) == a1 ** 2):
        maximum = max(a1, b1, c1)
        ans = maximum ** 2
    else:
        ans = 0
    return ans


squares3(a, b, c)
