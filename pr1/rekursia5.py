def pow_helper(x, n):
    if n == 0:
        return 1.0
    half = pow_helper(x, n // 2)   
    if n % 2 == 0:
        return half * half
    return half * half * x


def my_pow(x, n):
    if n < 0:
        return 1.0 / pow_helper(x, -n)
    return pow_helper(x, n)

print(f"{my_pow(2.0, 10):.5f}")    # 1024.00000
print(f"{my_pow(2.1, 3):.5f}")     # 9.26100
