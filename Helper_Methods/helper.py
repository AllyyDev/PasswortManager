from Helper_Methods import menu


def validate_password_search(password: str, user):
    wahl = None
    for credential in user["data"]:
        if credential["password"] == password:
            print(f"Benutzername: {credential['username']}")
            print(f"Password: {credential['password']}")
            wahl = menu.show_management_menu()
        else:
            print("Passwort nicht gefunden.")

    return wahl

def passwort_verwalten(wahl: int):
    match wahl:
        case 1:
            pass
        case 2:
            pass

def passwort_loeschen():
    pass