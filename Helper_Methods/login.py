import hashlib

def login(data: dict, username: str, password: str) -> dict:
    """
    Does a login attempt with given credentials.

    Args:
        username (str): Username
        password (str): Password

    Returns:
        dict: App data dictionary
        :param password:
        :param username:
        :param data:
    """
    hashed_passwort = passwort_hash(password)
    for user in data["users"]:
        if user["accountName"] == username and user["masterPassword"] == hashed_passwort:
            return user

    return None

def passwort_hash(password: str) -> str:
    return hashlib.sha256(password.encode()).hexdigest()