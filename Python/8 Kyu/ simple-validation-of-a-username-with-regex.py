def validate_usr(username):
    return 4 <= len(username) <= 16 and username == username.lower() and " " not in username
