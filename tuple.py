# WAP to enter a tuple as a first element as a number and second element as square

a = int(input("Enter first element: "))
b = int(input("Enter size of tuple: "))
for i in range(a, b+1, 1):
    square = i*i
    c = (i, square)
    print(c)
