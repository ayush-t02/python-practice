def calculate(a, b, formula):
    if formula == '+':
        return f"The answer is {a + b}"
    elif formula == '-':
        return f"The answer is {a - b}"
    elif formula == '*':
        return f"The answer is {a * b}"
    elif formula == '/':
        return f"The answer is {a / b}"
    else:
        print('Invalid operator')


a = float(input('Enter a number: '))
b = float(input('Enter another number: '))

formula = input('Choose operation: * / - + : ')
answer = calculate(a, b, formula)
print(answer)
