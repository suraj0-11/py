def fibonacci(n):
    if n <= 0:
        return None
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        a, b = 0, 1
        i = 3
        while i <= n:
            a, b = b, a + b
            i += 1
        return b

N = int(input("Enter a positive integer value for N: "))

if N <= 0:
    print("Invalid input. N must be a positive integer greater than 0.")
else:
    result = fibonacci(N)
    if result is not None:
        print(f"The {N}th term in the Fibonacci sequence is: {result}")
