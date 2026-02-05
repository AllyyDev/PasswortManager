from Helper_Methods import menu
import storage


def validate_password_search(password: str, user: dict):
    for credential in user["data"]:
        if credential["password"] == password:
            print(f"Benutzername: {credential['username']}")
            print(f"Password: {credential['password']}")
            option = menu.show_management_menu()
            return option

    print("Passwort nicht gefunden.")

    return None

def manage_password(option: int, password: str, user: dict):
    deleted_user = None
    match option:
        case 1:
            deleted_user = delete_password(password, user)
        case _:
            print("Menü wird aufgerufen")

    return deleted_user


def delete_password(password: str, user):
    for credential in user["data"]:
        if password in credential["password"]:
            credential["password"] = ""
            return user

    print("Fehler beim Löschen aufgetaucht!")
    return None

def save_user_to_db(db: dict, user: dict, username: str):
    """
    Saves a user to the JSON File
    :param db:
    :param user:
    :param username:
    :return:
    """
    target = next(
        (u for u in db["users"] if u["accountName"] == username),
        None
    )
    if not target:
        return

    existing = {c["username"]: c for c in target["data"]}

    for new_cred in user["data"]:
        existing[new_cred["username"]] = new_cred

    target["data"] = list(existing.values())
    storage.save(db)