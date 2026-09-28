def fib_helper(n, a, b):
    if n == 0:
        return a
    return fib_helper(n - 1, b, a + b)


def fib(n):
    return fib_helper(n, 0, 1)


if __name__ == "__main__":
    print(fib(0))   # 0
    print(fib(1))   # 1
    print(fib(2))   # 1
    print(fib(3))   # 2
    print(fib(4))   # 3
    print(fib(10))  # 55