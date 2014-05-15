def safe_input(prompt):
    try:
        input_ = raw_input(prompt)
    except (KeyboardInterrupt, EOFError):
        return None
    else:
        return unicode(input_)
