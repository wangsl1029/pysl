import hashlib, time

def token(username):
    """传入用户名，生成token"""
    API_SECRET = "Wsl19911991lsW"
    time_stamp = str(time.time())
    token = hashlib.md5()
    token.update((API_SECRET + time_stamp).encode("utf-8"))
    return token.hexdigest()


if __name__ == "__main__":
    print(token("wsongl"))