def fib(n):
    if n<=0:
        print("Number must be greater than zero")
        return
    elif n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fib(n-1) + fib(n-2)
    
n = int(input("Enter the number : "))
res = fib(n)
if res is not None:
    print(f"The {n}th term of the Fibonacci sequence is: {res}")