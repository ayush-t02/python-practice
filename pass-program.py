a = []
n = int(input("Enter number of elements: "))
print("Enter the elements: ")
for i in range(n):
    a.append(int(input()))

for i in a:
    if i < 0:
        print(i)
        pass
