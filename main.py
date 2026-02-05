from Helper_Methods import (
    removal, login, menu, display, addition
)
import storage


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
                password = menu.password_input()
                password_option = removal.validate_password_search(password, user)
                deleted_user_dict = removal.manage_password(password_option, password, user)

                if deleted_user_dict is not None:
                    removal.save_user_to_db(json_db, deleted_user_dict, username)
            case 2:
                display.display_all_passwords(user)
            case 3:
                create_password_option = menu.show_create_menu()
                password = addition.manage_new_password(create_password_option)

                if password is not None:
                    addition.save_password_to_database(json_db, password, username)
            case 4:
                print("Anwendung wird geschlossen...")
                break
            case _:
                print("Ungültige Eingabe!")
        option = menu.show_main_menu()

main()
