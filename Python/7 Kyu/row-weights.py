def row_weights(array):
    team1, team2 = 0, 0
    for i in range(0, len(array), 2):
        team1 += array[i]
    for i in range(1, len(array), 2):
        team2 += array[i]
    return (team1, team2)
