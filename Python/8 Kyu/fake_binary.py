def fake_bin(x):
    list = ""
    for i in x:
        if int(i) < 5:
            list += ("0")
        else:
            list += ("1")
    return list
            
