from Helper_Methods import helper, login, menu
import storage
from Helper_Methods.helper import delete_password


def main():
    username, master_password = menu.show_login_menu()
    json_db = storage.load()
    user = login.login(json_db, username, master_password)

    if user is None:
        print("Falsche Benutzereingaben!\n--------------------\n")
        main()

    option = menu.show_main_menu()

    while option != 4:
        match option:
            case 1:
                password = menu.search_password()
                password_option = helper.validate_password_search(password, user)
                deleted_user_dict = helper.manage_password(password_option, password, user)

                if deleted_user_dict is not None:
                    helper.save_user_to_db(json_db, deleted_user_dict, username)
            case 2:
                pass # Abrufen aller Passwörter
            case 3:
                # Passwort Eingabe und Passwort Generierung müssen noch implementiert werden
                menu.show_create_menu()
            case 4:
                print("Anwendung wird geschlossen...")
                break
            case _:
                print("Ungültige Eingabe!")
        option = menu.show_main_menu()

main()
