"""Lambda and keyword magic assignment"""

def function_builder(n):
    return [(lambda x, i=iterate: x + i) for iterate in range(n)]
