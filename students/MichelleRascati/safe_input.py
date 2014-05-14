def safe_input(err):
    """Return None rather than raising errors EOFError or KeyboardInterrupt"""
    if err == EOFError or err == KeyboardInterrupt:
        return None
    else:
        return err
