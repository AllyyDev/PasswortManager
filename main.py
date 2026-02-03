import menu, login, helper

def main():
    username, master_password = menu.login_menu()
    user = login.login(username, master_password)

    if user is None:
        print("Falsche Benutzereingaben!\n--------------------\n")
        main()

    wahl = menu.menu()

    while wahl != 4:
        match wahl:
            case 1:
                passwort = menu.passwort_suche()
                helper.validate_password_search(passwort, user)
            case 2:
                pass # Abrufen aller Passwörter
            case 3:
                # Passwort Eingabe und Passwort Generierung müssen noch implementiert werden
                menu.passwort_erstellen()
            case 4:
                pass
            case _:
                print("Ungültige Eingabe!")
        wahl = menu.menu()

main()
