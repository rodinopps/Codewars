def printer_error(s):
    errors = 0
    for i in s:
        if i not in "abcdefghijklm": errors += 1
    return f"{errors}/{len(s)}"
