def name_Error(num):
    c=num
    a=b+c
def type_Error(str):
    return sum(str)
def syntax_Error(str):
    retrn sum(str)
def attribute_Error(num):
    alwaysAnum = 7
    alwaysAnum.lower()
    return num

attribute_Error(4)
syntax_Error("hello")
type_Error("hello world")
name_Error(3)

#I commented out everything that prevents it from building.
#It's insteresting that it finds the syntax error within an uncalled function,
#but doesn't find the other errors.

#testing for commit stuff...
