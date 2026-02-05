from Helper_Methods import menu
import storage


def validate_password_search(password: str, user: dict) -> int:
    for credential in user["data"]:
        if credential["password"] == password:
            print(f"Benutzername: {credential['username']}")
            print(f"Password: {credential['password']}")
            option = menu.show_management_menu()
            return option

    print("Passwort nicht gefunden.")

    return -1

def manage_password(option: int, password: str, user: dict) -> dict:
    deleted_user = None
    match option:
        case 1:
            deleted_user = delete_password(password, user)
        case _:
            print("Menü wird aufgerufen...\n\n")

    return deleted_user


def delete_password(password: str, user: dict) -> dict:
    user["data"] = [
        cred for cred in user["data"]
        if cred["password"] != password
    ]

    return user

def save_user_to_db(db: dict, user: dict, account_name: str):
    """
    Saves a user to the JSON File
    :param db:
    :param user:
    :param account_name:
    :return:
    """
    target = next(
        (u for u in db["users"] if u["accountName"] == account_name),
        None
    )
    if not target:
        return

    target["data"] = user["data"]
    storage.save(db)