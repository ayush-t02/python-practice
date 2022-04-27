import math

# Check for perfect square
def checkPerfectSquare(n):
    root = math.sqrt(n)
    if int(root + 0.5) ** 2 == n:
        return True
    else:
        return False

def checkfibo(num):
    num1 = checkPerfectSquare((5 * num * num) + 4)
    num2 = checkPerfectSquare((5 * num * num) - 4)

    return num1 or num2

number = int(input("Enter a number to be checked: "))
print(checkfibo(number))
