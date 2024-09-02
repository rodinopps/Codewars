def whatday(num):
    if 1 <= num <= 7:
        return {1: "Sunday", 2: "Monday", 3: "Tuesday", 4: "Wednesday", 5: "Thursday", 6: "Friday", 7: "Saturday"}[num]
    else:
        return "Wrong, please enter a number between 1 and 7"
