def better_than_average(class_points, your_points):
    if your_points > sum(class_points) / len(class_points):
        return True
    else:
        return False
