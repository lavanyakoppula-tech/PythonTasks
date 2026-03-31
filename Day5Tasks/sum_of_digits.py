def sum_d(n):
    if n == 0:
        return 0
    return n % 10 + sum_d(n // 10)

print(sum_d(123))
