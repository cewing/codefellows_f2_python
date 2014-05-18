"""Safe input assignment"""

def safe_input():
    """Get user input or return None"""
    try:
        user_in = raw_input(">>> ")
    except (EOFError, KeyboardInterrupt):
        return None
    else:
        return user_in
