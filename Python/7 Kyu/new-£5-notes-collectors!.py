def get_new_notes(salary,bills):
    left = salary - sum(bills)
    if left <= 0:
        return 0
    else:
        return (salary - sum(bills)) // 5
