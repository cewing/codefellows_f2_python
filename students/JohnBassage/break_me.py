
def breaker_one():
    #intended to produce a NameError
    a = 10
    return a + b 


def breaker_two():
    #intended to produce a TypeError
    a = 10
    b = "string"
    return a/b

def breaker_three():
    #intended to produce a SyntaxError
    a = 10
    a +

def breaker_four():
    #intended to produce an AttributeError
    a = 10
    a.startswith("fix")

