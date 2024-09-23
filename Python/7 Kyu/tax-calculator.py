def tax_calculator(total):
    if total == None or total == str(total) or total == [] or total == {} or total <= 0:
        return 0
    elif 0 < total <= 10:
        return round(total * 0.1, 2)
    elif 10 < total <= 20:
        return round((total - 10) * 0.07 + 1, 2)
    elif 20 < total <= 30:
        return round((total - 20) * 0.05 + 1.7, 2)
    else:
        return round((total - 30) * 0.03 + 2.2, 2)
