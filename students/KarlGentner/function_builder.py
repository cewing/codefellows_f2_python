# Returns a list of n functions, which when called returns the input
# value incremented by an increasing number


def function_builder(n):
    list = []
    for i in range(n):
        list.append(lambda x, y=i: x + y)
    return list
