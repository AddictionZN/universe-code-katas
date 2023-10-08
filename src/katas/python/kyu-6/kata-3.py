# Function to calculate the N-th Fibonacci number
def nth_fib(n):
    # Base case: the first Fibonacci number is 0
    if n == 1:
        return 0
    # Base case: the second Fibonacci number is 1
    elif n == 2:
        return 1
    # Recursive case
    else:
        # Initializing the first two Fibonacci numbers
        first = 0
        second = 1
        # Variable to store the N-th Fibonacci number
        nth = 0
        # Loop to calculate the N-th Fibonacci number
        for _ in range(2, n):
            nth = first + second
            first, second = second, nth
        return nth


# Test the function
print(nth_fib(4))  # Output should be 2
