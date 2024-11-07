def reverse_alternate(st):
    list = st.split()
    new = []
    for i in range(len(list)):
        if i % 2 == 0: new.append(list[i])
        else: new.append(list[i][::-1])
    return " ".join(new)
