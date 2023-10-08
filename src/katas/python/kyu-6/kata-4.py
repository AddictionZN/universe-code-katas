import math


def get_participants(handshakes):
    n = 0
    current_handshakes = 0

    while current_handshakes < handshakes:
        n += 1
        current_handshakes = n * (n - 1) // 2

    return n
