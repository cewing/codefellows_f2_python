# safe input exception handler
def safe_input(message):
    """Return raw input or return None if EOFError or KeyboardInterrupt."""
    while True:
        try:
            x = raw_input(message)
            return x
        except EOFError:
            return None
        except KeyboardInterrupt:
            return None