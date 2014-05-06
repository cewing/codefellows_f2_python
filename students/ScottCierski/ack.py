def ack(m, n):
    """This function returns the values for Ackermann's Function"""
    if m < 0 or n < 0:
        print('Only positive values are allowed.')
        return
    elif m > 0 and n == 0:
        print(ack(m-1, 1))
    elif m > 0 and n > 0:
        print(ack(m-1, ack(m, n-1)))

if __name__ == '__main__':
    ack(0, 0)
    ack(0, 1)
    ack(0, 2)
    ack(0, 3)
    ack(0, 4)
    ack(1, 0)
    # ack(1, 1)
    # ack(1, 2)
    # ack(1, 3)
    # ack(1, 4)
    # ack(2, 0)
    # ack(2, 1)
    # ack(2, 2)
    # ack(2, 3)
    # ack(2, 4)
    # ack(3, 0)
    # ack(3, 1)
    # ack(3, 2)
    # ack(3, 3)
    # ack(3, 4)
    # ack(4, 0)
    # ack(4, 1)
    # ack(4, 2)
    # ack(4, 3)
    # ack(4, 4)