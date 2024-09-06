def duty_free(price, discount, holiday_cost):
    save = holiday_cost / (price * discount / 100)
    return save // 1
