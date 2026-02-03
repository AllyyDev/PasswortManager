import os, json, hashlib

if os.path.exists("../database.json"):
    with open("../database.json", "r") as f:
        data = json.load(f)
else:
    data = {"users": []}

def login(username: str, password: str):
    hashed_password = passwort_hash(password)
    for user in data["users"]:
        if user["accountName"] == username and user["masterPassword"] == hashed_password:
            return user
    return None

def passwort_hash(password: str):
    return hashlib.sha256(password.encode()).hexdigest()