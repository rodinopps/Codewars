def number(bus_stops):
    on, left = 0, 0
    for i in bus_stops:
        on += i[0]
        left += i[1]
    return on - left
