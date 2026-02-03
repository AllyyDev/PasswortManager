import menu

def validate_password_search(password: str, user):
    for credential in user["credentials"]:
        if credential["password"] == password:
            print(f"Benutzername: {credential['username']}")
            print(f"Password: {credential['password']}")
            wahl = menu.passwort_verwaltung()
        else:
            print("Passwort nicht gefunden.")