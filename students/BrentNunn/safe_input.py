#!/usr/bin/env python

def safe_input(*prompt):
    """Wrapping raw_input() to catch typical end of input exceptions"""
    try:
        if len(prompt) > 0:
            user_in = raw_input(prompt[0])
        else:
            user_in = raw_input()

    except (KeyboardInterrupt, EOFError):
        return None
    else:
        return user_in

if __name__ == '__main__':
    print "Testing safe_input() function"
    print "^C or ^D to end"

    while True:
        get_input = safe_input("Type something: ")
        if get_input == None:
            print '\nTest complete'
            break
        else:
            print 'You entered: ', get_input
        
        print 'Testing with no prompt parameter, keep typing... '
        get_input = safe_input()
        if get_input == None:
            print '\nTest complete'
            break
        else:
            print 'You entered: ', get_input

