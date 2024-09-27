def michael_pays(cost):
    if cost < 5:
        return round(cost, 2)
    elif cost <= 30:
        return round(cost * 2/3, 2)
    else:
        return round(cost - 10, 2)
