def safe_input(prompt):
    try:
        raw_input(prompt)
    except KeyboardInterrupt:
        return None
    except EOFError:
        return None
