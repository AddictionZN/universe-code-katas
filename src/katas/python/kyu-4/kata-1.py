from collections import defaultdict
from math import sqrt


def prime_factors(n):
    factors = set()
    while n % 2 == 0:
        factors.add(2)
        n = n // 2

    for i in range(3, int(sqrt(n)) + 1, 2):
        while n % i == 0:
            factors.add(i)
            n = n // i

    if n > 2:
        factors.add(n)
    return factors


def sum_for_list(I):

    prime_sums = defaultdict(int)

    for i in I:
        factors = prime_factors(abs(i))
        for f in factors:
            prime_sums[f] += i

    P = [[k, v] for k, v in sorted(prime_sums.items())]
    return P
