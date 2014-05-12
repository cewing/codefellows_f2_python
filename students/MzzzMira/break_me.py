
def _name_error () :
    num = 45
    num += 1
    del num
    print num
    
def _type_error () :
    num = 3.4
    num = u'can be a string'
    print type(num)
    
def _syntax_error () :
    num = 5
    if num > 3
        print num
    
def _attribute_error () :
    num = 42
    print num.__fail__
