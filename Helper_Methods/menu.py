def show_main_menu() -> int:
    """
    Displays main menu.

    Returns:
        int: Selected entry
    """
    print("<<<<<<<<<< Willkommen zu SecPass >>>>>>>>>>\n")
    print("(1) Passwort suchen")
    print("(2) Alle Passwörter")
    print("(3) Neues Passwort")
    print("(4) Speichern/Exit")
    print("--------------------\n")

    inp = int(input("Wahl: "))
    return inp

def show_management_menu() -> int:
    """
    Displays management menu.

    Returns:
        int: Selected entry
    """
    print("")
    print("(1) Passwort löschen")
    print("(2) Menü\n--------------------\n")

    inp = int(input("Wahl: "))
    return inp

def show_create_menu() -> int:
    """
    Displays password create menu.

    Returns:
        int: Selected entry
    """
    print("")
    print("(1) Passwort eingeben")
    print("(2) Passwort generieren")
    print("(3) Menü\n--------------------\n")

    inp = int(input("Wahl: "))
    return inp

def search_password():
    passwort = input("Passwort: ")
    return passwort

def show_login_menu() -> tuple[str, str]:
    """
    Displays login menu.

    Returns:
        tuple[str, str]: Username and password
    """
    username = input("Benutzername: ")
    master_password = input("Master Passwort: ")
    return username, master_password