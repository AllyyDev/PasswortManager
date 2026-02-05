import storage
from Helper_Methods import checker, generator, menu

def manage_new_password(option: int) -> str:
    match option:
        case 1:
            password = menu.password_input()
            success, message = checker.check_password(password)
            if success:
                print(message)
                return password
            print(message)
            return manage_new_password(option)
        case 2:
            return generator.generate_password()
        case _:
            print("Menü wird aufgerufen")

    return ""



def save_password_to_database(db: dict, password: str, account_name: str):
    target = next(
        (u for u in db["users"] if u["accountName"] == account_name),
        None
    )
    if not target:
        return

    new_creds = {
        "username": "",
        "password": password
    }

    target["data"].append(new_creds)

    storage.save(db)

