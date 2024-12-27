def is_valid_walk(walk):
    north = walk.count("n")
    south = walk.count("s")
    east = walk.count("e")
    west = walk.count("w")
    up = north * 90 - south * 90
    side = east * 90 - west * 90
    return len(walk) == 10 and up == 0 and side == 0
