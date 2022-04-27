n = int(input("Enter limit for series: "))


def fibo(a, b):
    print(a)
    print(b)
    for i in range(0, n - 2):
        c = a + b
        a = b
        b = c
        print(c)


fibo(0, 1)
