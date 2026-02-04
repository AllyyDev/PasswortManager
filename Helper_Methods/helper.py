from Helper_Methods import menu
import storage


def validate_password_search(password: str, user: dict):
    option = None
    for credential in user["data"]:
        if credential["password"] == password:
            print(f"Benutzername: {credential['username']}")
            print(f"Password: {credential['password']}")
            option = menu.show_management_menu()
        else:
            print("Passwort nicht gefunden.")

    return option

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
            del credential["password"]
        else:
            print("Fehler beim Löschen aufgetaucht!")

    return user

def save_user_to_db(db: dict, user: dict, username: str):
    """

    :param db:
    :param user:
    :param username:
    :return:
    """
    for current_user in db["users"]:
        if current_user["accountName"] == username:
            for credential in current_user["data"]:
                for user_data in user["data"]:
                    if credential["username"] == user_data["username"]:
                        current_user["data"].remove(credential)
                        current_user["data"].append(user_data)
                        storage.save(db)
                        break