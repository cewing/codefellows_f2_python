def return_p_wrapped_string(func):
    """asd"""
    def p_wrapper(string):
        result = "<p>" + string + "</p>"
        print result
        return result
    return p_wrapper

# Decorator, using declaritave form
@return_p_wrapped_string
def return_string(string):
    """Returns a given string."""
    return string

# Set return_string to the result of the wrapped return_string
return_string = return_p_wrapped_string(return_string)


if __name__ == '__main__':
    return_string("This is some paragraph text.")