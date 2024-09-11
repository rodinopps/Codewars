def elevator(left, right, call):
    if abs(left - call) >= abs(right - call):
        return "right"
    elif abs(right - call) > abs(left - call):
        return "left"
