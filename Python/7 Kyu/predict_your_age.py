def predict_age(a1, a2, a3, a4, a5, a6, a7, a8):
    new = [a1 * a1, a2 * a2, a3 * a3, a4 * a4, a5 * a5, a6 * a6, a7 * a7, a8 * a8]
    return int((sum(new) ** 0.5) / 2)
