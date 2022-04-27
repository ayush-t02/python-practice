# WAP to search an element in list

a = []
n = int(input("Enter number of elements: "))
print("Enter the elements: ")
for i in range(n):
    a.append(int(input()))

target = int(input("Enter element to be searched: "))
for i in a:
    if i == target:
        print("Element found")
        break
