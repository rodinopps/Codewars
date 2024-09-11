def generate_hashtag(s):
    hashtag = "#" + s.title().replace(" ", "")
    if len(hashtag) > 140 or s == "": return False
    else: return hashtag
