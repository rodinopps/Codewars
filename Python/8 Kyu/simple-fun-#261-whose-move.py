def whose_move(last_player, win):
    if last_player == "white" and win == False or last_player == "black" and win == True: return "black"
    else: return "white"
