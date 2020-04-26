import hashlib
import random
import string
import time


def token(username):
    """传入用户名，生成token"""
    rand_secret = ''.join(random.sample(string.ascii_letters + string.digits, 8))
    time_stamp = str(time.time())
    token = hashlib.md5()
    token.update((rand_secret + time_stamp + username).encode("utf-8"))
    return token.hexdigest()


if __name__ == "__main__":
    print(token("wsongl"))
