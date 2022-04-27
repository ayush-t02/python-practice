def prime_check(num):
    count = 0
    for i in range(2, n):
        if n % i == 0:
            count += 1

    if count == 0:
        print("number is prime")
    else:
        print("not prime")


n = int(input("Enter the no. to be checked: "))
prime_check(n)
