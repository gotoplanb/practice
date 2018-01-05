def is_isogram(string):
    """Determine if the string has any repeating letters."""

    previous = []

    for current in string:
        current = current.lower()
        if (current == "-") or (current == " "):
            pass
        elif current in previous:
            return False
        else:
            previous.append(current)

    return True
