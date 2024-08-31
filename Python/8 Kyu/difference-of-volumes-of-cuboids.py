def find_difference(a, b):
    vola = 1
    volb = 1
    for i in a:
        vola *= i
    for i in b:
        volb *= i
    return abs(vola - volb)
