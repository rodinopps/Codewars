def shark(pontoon_distance, shark_distance, you_speed, shark_speed, dolphin):
    if dolphin:
        if pontoon_distance / you_speed > shark_distance / (shark_speed / 2): return "Shark Bait!"
        else: return "Alive!"
    else:
        if pontoon_distance / you_speed > shark_distance / (shark_speed): return "Shark Bait!"
        else: return "Alive!"
