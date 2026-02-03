import menu

def validate_password_search(password: str, user):
    wahl = None
    for credential in user["credentials"]:
        if credential["password"] == password:
            print(f"Benutzername: {credential['username']}")
            print(f"Password: {credential['password']}")
            wahl = menu.passwort_verwaltung()
        else:
            print("Passwort nicht gefunden.")

    return wahl

def passwort_verwalten(wahl: int):
    match wahl:
        case 1:
            pass
        case 2:
            pass