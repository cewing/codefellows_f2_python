# Karl Gentner - cff2py - break_me.py 05/07/2014

# Name Error Example
# "unfoundName" not declared globally
# or locally


def myNameError():
    return unfoundName


# Type Error Example
# absolute value can not operate on a string


def myTypeError():
    return abs("four")


# SyntaxError Example
# misplaced colon after return


def mySyntaxError():
    return: "syntax shmyntax"


# Attribute Error Example
# there is no .length attribute for integers


def myAttributeError():
    x = 3
    return x.length


# Toggle comments to run functions

# myNameError()
# myTypeError()
# mySyntaxError()
# myAttributeError()
