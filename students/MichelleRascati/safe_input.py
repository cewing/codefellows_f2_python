def safe_input(safe_string):
    """Do not raise EOFError or KeyboardInterrupt for raw_input()"""
    try:
        raw_input(safe_string)
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        return safe_string

if __name__ == '__main__':
    assert safe_input('hello') == True 
