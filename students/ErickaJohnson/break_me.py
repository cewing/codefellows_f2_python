#Create a new file called break_me.py.
#Create it inside your personal folder in the students folder
#of the class repository
#Make sure you create it in your clone of your fork of the
#repository.
#Use git add to add the file to the repository.
#In the file write four simple Python functions
#Each function, when called, should cause an exception to happen
#Each function should result in one of the four common exceptions from our
#lecture.
#for review: NameError, TypeError, SyntaxError, AttributeError
#Use the Python standard library reference on Built In Exceptions as a
#reference

def Name():
    u"""Raises a NameError."""
    print s # Variable s is not defined.

def Type():
    u"""Raises a TypeError."""
    print 4/u"the" # 4 is an int; "the" is a string. 
        #Math can't be done with non-ints or non-floats.

def Syntax(n):
    u"""Raises a SyntaxError."""
    if 4 > n #There should be a semi-colon at the end of this line.
        print u"n is smaller than 4."

def Attribute(n): #*************This is throwing up a SyntaxError instead. Come back to this.**************************
    u"""Raises a AttributeError."""
    print 5.lower() #5 is an int and can't be turned into a lowercase.