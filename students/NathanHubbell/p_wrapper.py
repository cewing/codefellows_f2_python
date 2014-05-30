def p_wrapper(func):
    def wrapped(*args, **kwargs):
        the_string = func(*args, **kwargs)
        the_string="<p>%s<p>"%the_string
        return the_string
    return wrapped

@p_wrapper
def return_a_string(ianput):
    return ianput*5

@p_wrapper
@p_wrapper
def return_an_int(integer):
    return integer*5

print return_a_string("hello")

print return_an_int(5)