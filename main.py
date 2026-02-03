from Helper_Methods import helper, login, menu
import storage


def main():
    username, master_password = menu.show_login_menu()
    user = login.login(storage.load(), username, master_password)

    if user is None:
        print("Falsche Benutzereingaben!\n--------------------\n")
        main()

    wahl = menu.show_main_menu()

    while wahl != 4:
        match wahl:
            case 1:
                passwort = menu.search_password()
                helper.validate_password_search(passwort, user)
            case 2:
                pass # Abrufen aller Passwörter
            case 3:
                # Passwort Eingabe und Passwort Generierung müssen noch implementiert werden
                menu.show_create_menu()
            case 4:
                pass
            case _:
                print("Ungültige Eingabe!")
        wahl = menu.show_main_menu()

main()
