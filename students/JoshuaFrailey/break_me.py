def causeNameError():
    '''
    Causes a NameError
    '''
    return moose

def causeTypeError():
    '''
    Causes a TypeError
    '''
    notAString = 45315
    for letter in notAString:
        print letter

def causeAttributeError():
    a = 5
    a.sort()