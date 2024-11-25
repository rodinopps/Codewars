def weather_info (temp):
    t = (temp - 32) * (5/9)
    if t < 0:
        return (f"{t} is freezing temperature")
    else:
        return (f"{t} is above freezing temperature")
