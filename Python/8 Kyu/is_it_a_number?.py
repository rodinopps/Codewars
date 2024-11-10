def is_digit(s):
    try:
        float(s.strip())
        return True
    except:
        return False
