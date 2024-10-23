def fuel_price(litres, price_per_litre):
    if 2 <= litres < 4: total = round(litres * (price_per_litre - 0.05), 2)
    elif 4 <= litres < 6: total = round(litres * (price_per_litre - 0.1), 2)
    else: total = round(litres * (price_per_litre - 0.25), 2)
    return round(total * 100) / 100
