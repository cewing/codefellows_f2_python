# Amanda L. Moen
# cff2py
# break_me.py

#Write four simple Python functions.
#    NameError:  indicates that you have tried to use a symbol that is not bound to a value.
#    TypeError: indicates that you have tried to use the wrong kind of object for an operation.
#    SyntaxError: indicates that you have mis-typed something.
#    AttributeError: indicates that you have tried to access an attribute or method that an 
#    object does not have (this often means you have a different type of object than you expect)

# NameError define a function that will raise a NameError exception
# An error occurs because 'b' was not defined.
def break_name():
    a = 2
    return a + b

# TypeError define a function that will raise a TypeError exception.
# An error occurs because the program is trying to add 2 different data types.
def break_type():
    print 1 + 'Hello World!'

# SyntaxError define a function that will raise a SyntaxError exception.
# An error occurs because else cannot be used as a symbol.
def break_syntax():
    print else

# AttributeError define a function that will raise an AttributeError exception.
def break_attribute(str):
    a = 'hello'
    a.hello
