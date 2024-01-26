def cal_factorial(n):
    hold_multiply = 1
    while n > 0:
        hold_multiply = hold_multiply * n  # m = 5, n=4, m = m(5) * n(4), m = 20 * 3 = 60 * 2 = 120 * 1
        n = n - 1  # 4, 3, 2, 1, 0
    return hold_multiply


n_str = input()
n_int = int(n_str)
fact = cal_factorial(n_int)
print(f"factorial of number {n_int} = ", fact)


