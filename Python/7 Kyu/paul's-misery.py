def paul(x):
    misery = 0
    values = {"kata": 5, "Petes kata": 10, "life": 0, "eating": 1}
    for i in x:
        misery += values[i]
    if misery < 40: return "Super happy!"
    elif 40 <= misery < 70: return "Happy!"
    elif 70 <= misery < 100: return "Sad!"
    else: return "Miserable!"
