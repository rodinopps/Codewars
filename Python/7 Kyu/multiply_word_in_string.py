def modify_multiply(st, loc, num):
    list = st.split()
    new = []
    for i in range(num):
        new.append(list[loc])
    return "-".join(new)
