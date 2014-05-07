def fibonacci(n):
    """Return nth number in fibonacci sequence"""
    # Initialize sequence
    seq = [0, 1]
    if n == 1:
        return 0
    elif n == 2:
        return 1
    for i in range(1, n - 1):
        seq = seq.append(seq[i] + seq[i - 1])
    return seq[-1]