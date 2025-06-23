from .exceptions import InvalidOperationError

def parse_number(token):
    try:
        return float(token)
    except ValueError:
        raise InvalidOperationError(f"Invalid number '{token}'")

def parse_command(tokens):
    cmd = tokens[0].lower()
    args = tokens[1:]
    return cmd, args
