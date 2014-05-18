def safe_input():
    """Wrapper around raw_input() to return None instead of exceptions"""

    try:
        input_string = raw_input('Enter any input: ')
    except KeyboardInterrupt:
        print u""
        print u"You initiated a keyboard interrupt. Good bye."
        return None
    except EOFError:
        print u""
        print u"You reached the End Of File. Good bye."
        return None
    else:
        print input_string

if __name__ == '__main__':
    safe_input()