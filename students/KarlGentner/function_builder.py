# Returns a list of n functions, which when called returns the input
# value incremented by an increasing number


def function_builder(n):
    list = [lambda x, y=i: x+y for i in range(n)]
    return list