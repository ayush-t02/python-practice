# 1. Arithmetic
try:
    a = 10 / 0
    print(a)
except ArithmeticError:
    print("This statement is raising an arithmetic exception.")
else:
    print("Success.")

# 2. Lookup
try:
    a = [1, 2, 3]
    print(a[3])
except LookupError:
    print("Index out of bound error.")
else:
    print("Success")

# 3. EOF
while True:
    data = input('Enter name : ')
    print('Hello ', data)
    break

# 4. Keyboard Interrupt
try:
    print('Press Return or Ctrl-C:', )
    ignored = input()
except Exception as e:
    print('Caught exception:', e)
except KeyboardInterrupt as k:
    print('Caught KeyboardInterrupt', k)
else:
    print('No exception')


# 5. Memory
def fact(a):
    factors = []
    for i in range(1, a + 1):
        if a % i == 0:
            factors.append(i)
    return factors


num = 600851475143
print(fact(num))
