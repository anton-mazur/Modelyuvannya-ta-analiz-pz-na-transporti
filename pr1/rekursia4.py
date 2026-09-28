def climb_helper(n, a, b):
    # a = ways(k), b = ways(k+1)
    if n == 0:
        return a
    return climb_helper(n - 1, b, a + b)


def climb_stairs(n):
    return climb_helper(n - 1, 1, 2)



print(climb_stairs(1))   # 1
print(climb_stairs(2))   # 2
print(climb_stairs(3))   # 3
print(climb_stairs(4))   # 5
print(climb_stairs(5))   # 8
print(climb_stairs(45))  # 1836311903