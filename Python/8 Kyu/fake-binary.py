def fake_bin(x):
    fake = ""
    for i in x:
        if int(i) < 5:
            fake += "0"
        else:
            fake += "1"
    return fake
