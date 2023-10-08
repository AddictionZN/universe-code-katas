import math

def litres(time):
    # Nathan drinks 0.5 litres of water per hour of cycling.
    total_litres = time * 0.5
    
    # Round down to the nearest whole number.
    return math.floor(total_litres)


# Test the function
print(litres(3))  # Should return 1
print(litres(6.7))  # Should return 3
print(litres(11.8))  # Should return 5