def is_opposite(s1,s2):
    if s1 == "":
        return False
    else:
        for i in range(len(s1)):
            if s1[i] == s2[i]:
                return False
 
    return True
