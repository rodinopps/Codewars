def sum_of_a_beach(beach):
    sand = beach.lower().count("sand")
    water = beach.lower().count("water")
    fish = beach.lower().count("fish")
    sun = beach.lower().count("sun")
    return sand + water + fish + sun
