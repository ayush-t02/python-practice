# 1. Factorial
n = int(input("Enter a number: "))
def factorial(n):
    fact = 1
    for num in range(2, n + 1):
        fact = fact * num
    return(fact)
print("Factorial = ", factorial(n))
print()

# 2. Reversing a string using slicing
s = input("Enter a string: ")
reverse = s[::-1]
print(f"Reverse of {s} is: {reverse}")
