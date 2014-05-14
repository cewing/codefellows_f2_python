def safe_input(prompt):
    try:
        input_ = raw_input(prompt)
    except KeyboardInterrupt:
        return None
    except EOFError:
        return None
    else:
        return unicode(input_)
