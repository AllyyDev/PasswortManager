import storage
from Helper_Methods import checker, generator, menu

def manage_new_password(option: int) -> tuple[str, str]:
    """
    Manages new credentials.

    Returns:
        username and password

    :param option:
    :return:
    """
    match option:
        case 1:
            username = input("Benutzername: ")
            password = menu.password_input()
            success, message = checker.check_password(password)
            if success:
                print(message)
                return username, password
            print(message)
            return manage_new_password(option)
        case 2:
            username = input("Benutzername: ")
            password = generator.generate_password()

            print("\n\nNeue Kredentiale:")
            print("Benutzername: ", username)
            print("Passwort: ", password )
            print("\n------------------------------\n")
            return username, password
        case _:
            print("Menü wird aufgerufen...\n\n")

    return "", ""



def save_password_to_database(db: dict, new_user: str, password: str, account_name: str):
    """
    Saves new credentials into database.
    :param db:
    :param new_user:
    :param password:
    :param account_name:
    :return:
    """

    target = next(
        (u for u in db["users"] if u["accountName"] == account_name),
        None
    )
    if not target:
        return

    new_creds = {
        "username": new_user,
        "password": password
    }

    target["data"].append(new_creds)

    storage.save(db)

