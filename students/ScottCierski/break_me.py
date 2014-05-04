# This file contains functions that will deliberately fail

# This function will cause a NameError because x is not defined anywhere
def cause_name_error():
    print(x)

 # This function will cause a TypeError because it attempts to add two different data types (int and string)
def cause_type_error():
    print 1 + 'I am a string'

# This function will cause a syntax error because it tries to execute invalid Python (1 + a missing value)
def cause_syntax_error():
    print 1 + 

# This function will cause an AttributeError because it tries to find a "lower" attribute on an integer
def cause_attribute_error():
    x = 1
    print(x.lower())

# Useful for running a single function from the command line
# if __name__ == '__main__':
#     cause_attribute_error()