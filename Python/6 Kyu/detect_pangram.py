def is_pangram(st):
    check = []
    for i in st.lower():
        if i not in check and i in "abcdefghijklmnopqrstuvwxyz":
            check.append(i)
    return len(check) == 26
