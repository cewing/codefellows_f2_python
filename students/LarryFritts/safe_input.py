"""Safe Input Function"""

def safe_input(msg):
    """Used to handle ^C and ^D"""
    try:
        variable = raw_input(msg)
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        return variable

if __name__ == "__main__":
    my_string = safe_input("Input: ")
    print my_string