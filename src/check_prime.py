def is_prime(n):
    # Either Prime or Not Prime
    # If prime return True
    # else return False

    # Prime Number: A number is prime if and only it is divisible by 1 and
    # itself To check it programmatically we check if a number is divisible
    # by in range of (2..n-1), if any number in this range is dividing the
    # given number n that means number is not prime, otherwise number is prime.

    # 5 (2, n - 1) => (2, 3, 4)
    # 9 (2, n - 1) => 2, 3, 4, 5,... 8
    start = 2
    while start < n:
        if n % start == 0:
            return False
        start = start + 1
    return True


n_str = input()
n_int = int(n_str)
is_prime = is_prime(n_int)
print(f"Is Number Prime {n_int} = ", is_prime)
