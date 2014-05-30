def fibonacci(n):
    """Return nth number in the Fibonacci sequence."""
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
    """Return nth number in the Lucas numbers."""
    # Initialize sequence
    seq = [2, 1]
    if n == 1:
        return 2
    elif n == 2:
        return 1
    for i in range(1, n - 1):
        seq.append(seq[i] + seq[i - 1])
    return seq[-1]


def sum_series(n, first=0, second=1):
    """Return nth number in sum series beginning with 'first' and 'second'."""
    seq = [first, second]
    if n == 1:
        return first
    elif n == 2:
        return second
    for i in range(1, n - 1):
        seq.append(seq[i] + seq[i - 1])
    return seq[-1]
