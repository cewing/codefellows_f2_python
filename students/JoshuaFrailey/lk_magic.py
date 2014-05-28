def function_builder(x):
    return [lambda j, i=q: i+j for q in range(x)]