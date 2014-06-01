def generator_sum_of_integers(stop):
    """
    Keep adding the next integer, so: 0 + 1 + 2 + 3 + 4 + 5 + ...
    ... yields the sequence: 0, 1, 3, 6, 10, 15 .....
    """

    current_sum = 0

    for i in range(stop):
        current_sum = i + current_sum
        yield current_sum
        i =+ 1


def generator_doubler(stop):
    """
    Generator which yields each value double the previous value:
    1, 2, 4, 8, 16, 32...
    """

    current_product = 1

    # Seed initial result
    yield current_product
    
    for i in range(1, stop):
        current_product = current_product * 2
        yield current_product
        i = i * 2


def fibonacci(n):
    """
    Fibonacci sequence recursive function: f(n) = f(n-1) + f(n-2)
    """

    if n < 2:
        return n
    else:
        return fibonacci(n-2) + fibonacci(n-1)


def generator_fibonacci_sequence(stop):
    """
    Generator which yields Fibonacci sequence: f(n) = f(n-1) + f(n-2)
    1, 1, 2, 3, 5, 8, 13, 21, 34...
    """
    for i in range(stop):
        yield fibonacci(i)


def is_prime(n):
    '''Prime number checker'''

    # Do not consider negative numbers or 0 or 1
    if n < 2:
        return False
    # 2 is the only even prime number
    elif n == 2:
        return True
    # Do not consider any other even numbers
    elif n % 2 == 0:
        return False
    # Start at 3 and go up to squareroot of n
    else:
        for i in range(3, int(n**0.5)+1, 2):
            if n % i == 0:
                return False

    # Otherwise, it's a prime
    return True


def generator_prime_numbers(stop):
    """
    Generator which yields only prime numbers
    2, 3, 5, 7, 11, 13, 17, 19, 23...
    """
    for i in range(1, stop):
        if is_prime(i) == True:
            yield i


if __name__ == "__main__":

    test_stop = 30

    # Test generator_sum_of_integers()
    print u"Sum of Integers"
    for n in generator_sum_of_integers(test_stop):
        print n
    print u""

    # Test generator_doubler()
    print u"Doubler"
    for n in generator_doubler(test_stop):
        print n
    print u""

    # Test generator_fibonacci_sequence()
    print u"Fibonacci Sequence"
    for n in generator_fibonacci_sequence(test_stop):
        print n
    print u""

    # Test generator_prime_numbers()
    print u"Prime Numbers"
    for n in generator_prime_numbers(test_stop):
        print n
    print u""