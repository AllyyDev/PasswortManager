
def display_all_passwords(user: dict):
    print("Passwords found: ")
    for credential in user["data"]:
        print("Benutzername: ", credential["username"])
        print("Passwort: ", credential["password"])
        print()