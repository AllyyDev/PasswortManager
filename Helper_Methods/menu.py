def menu():
    print("<<<<<<<<<< Willkommen zu SecPass >>>>>>>>>>\n")
    print("(1) Passwort suchen")
    print("(2) Alle Passwörter")
    print("(3) Neues Passwort")
    print("(4) Speichern/Exit")

    inp = int(input("Wahl: "))
    return inp

def passwort_verwaltung():
    print("(1) Passwort löschen")
    print("(2) Menü\n--------------------\n")

    inp = int(input("Wahl: "))

    if inp is not [1, 2]:
        print("Ungültige Eingabe!")
        passwort_verwaltung()

    return inp

def passwort_erstellen():
    print("(1) Passwort eingeben")
    print("(2) Passwort generieren")
    print("(3) Menü\n--------------------\n")

    inp = int(input("Wahl: "))
    return inp

def passwort_suche():
    passwort = input("Passwort: ")
    return passwort

def login_menu():
    username = input("Benutzername: ")
    master_password = input("Master Passwort: ")
    return username, master_password

