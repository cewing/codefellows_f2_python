def ack(m, n):
    """This function returns the values for Ackermann's Function"""
    if m < 0 or n < 0:
        print('Only positive values are allowed.')
        return None
    elif m == 0:
        return(n+1)
    elif m > 0 and n == 0:
        return(ack(m-1, 1))
    elif m > 0 and n > 0:
        return(ack(m-1, ack(m, n-1)))

if __name__ == '__main__':
    print(ack(0, 0))
    print(ack(0, 1))
    print(ack(0, 2))
    print(ack(0, 3))
    print(ack(0, 4))
    print(ack(1, 0))
    print(ack(1, 1))
    print(ack(1, 2))
    print(ack(1, 3))
    print(ack(1, 4))
    print(ack(2, 0))
    print(ack(2, 1))
    print(ack(2, 2))
    print(ack(2, 3))
    print(ack(2, 4))
    print(ack(3, 0))
    print(ack(3, 1))
    print(ack(3, 2))
    print(ack(3, 3))
    print(ack(3, 4))
    print(ack(4, 0))
    print(ack(4, 1))
    print(ack(4, 2))
    print(ack(4, 3))
    print(ack(4, 4))