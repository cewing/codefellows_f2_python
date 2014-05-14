def safe_input(safe_string):
    """Do not raise EOFError or KeyboardInterrupt for raw_input()"""
    try:
        out = raw_input(safe_string)
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        return out

# Cant figure out how to write an assert statement for this
#if __name__ == '__main__':
#    assert safe_input('hello') == True
