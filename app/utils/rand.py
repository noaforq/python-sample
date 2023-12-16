import secrets
import string


def random_code() -> str:
    """8文字のランダムな文字列(a-zA-Z0-9)を返す"""
    size = 8
    pool = string.digits + string.ascii_letters
    code = "".join([secrets.choice(pool) for _ in range(size)])
    return code


def generate_password() -> str:
    """6文字のランダムな数字文字列を返す"""
    size = 6
    pool = string.digits
    password = "".join([secrets.choice(pool) for _ in range(size)])
    return password


def generate_auth_password() -> str:
    """8文字、大文字小文字数字それぞれ1文字以上を含むランダムな文字列を返す"""
    size = 8
    pool = string.digits + string.ascii_letters
    while True:
        password = "".join([secrets.choice(pool) for _ in range(size)])
        if any(c.islower() for c in password) and any(c.isupper() for c in password) and any(c.isdigit() for c in password):
            return password
