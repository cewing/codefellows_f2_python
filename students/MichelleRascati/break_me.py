def fun_name():
    #This should cause a NameError
    x = y+1

def fun_type():
    #This should cause a TypeError
    a = 'hello' + 1

def fun_syntax():
    #This should cause a SyntaxError
    fo i in range(5):
        print i

def fun_attribute():
    #This should cause an AttributeError
    string = 'hello'
    print string.strlwr()