def validate_pin(pin):
    if (len(pin) == 4 or len(pin) == 6) and pin.isdigit():
        return True
    else:
        return False
