def NameErrorFunction():
    a = 8
    return someVariable

def TypeErrorFunction():
    a = "This is a string"
    for i in range(a):
        print a[i]
    return a

def SyntaxErrorFunction():
    import somethingWeird
    a = 6
    return a

def AttributeErrorFunction():
    a = 145
    a.attribute = 7
    return a

#NameErrorFunction()
#TypeErrorFunction()
#SyntaxErrorFunction()
AttributeErrorFunction()