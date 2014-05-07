def fibonacci(n):
    """Return nth number in Fibonacci sequence"""
    # Initialize sequence
    seq = [0, 1]
    if n == 1:
        return 0
    elif n == 2:
        return 1
    for i in range(1, n - 1):
        seq.append(seq[i] + seq[i - 1])
    return seq[-1]


def lucas(n):
    """Return nth number in Lucas numbers"""
    # Initialize sequence
    seq = [2, 1]
    if n == 1:
        return 2
    elif n == 2:
        return 1
    for i in range(1, n - 1):
        seq.append(seq[i] + seq[i - 1])
    return seq[-1]
