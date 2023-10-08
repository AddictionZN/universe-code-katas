def dig_pow(n, p):
    # Step 1: Convert n to a list of its digits
    digits = [int(d) for d in str(n)]

    # Step 2: Calculate the sum of digits raised to the power p, p+1, ...
    total_sum = sum(d ** (p + i) for i, d in enumerate(digits))

    # Step 3: Check if total_sum is divisible by n
    k, remainder = divmod(total_sum, n)

    return k if remainder == 0 else -1
