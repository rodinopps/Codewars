def format_duration(seconds):
    if seconds == 0:
        return "now"

    time = [("years", 365 * 24 * 60 * 60),
        ("days", 24 * 60 * 60),
        ("hours", 60 * 60),
        ("minutes", 60),
        ("seconds", 1),]

    format = []
    for unit, duration in time:
        if seconds >= duration:
            count = seconds // duration
            seconds %= duration
            if count == 1: format.append(f"{count} {unit[:-1]}")
            else: format.append(f"{count} {unit}")

    if len(format) == 1: return format[0]
    else: return ", ".join(format[:-1]) + " and " + format[-1]
