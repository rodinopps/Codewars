def cube_times(times):
    times.sort()
    middle = len(times) // 2
    average = (times[middle - 1] + times[middle] + times[middle + 1]) / 3
    return (round(average, 2), min(times))
