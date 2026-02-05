
def display_all_passwords(user: dict):
    print("Passwords found: ")
    for credential in user["data"]:
        if credential["password"] != "":
            print(credential["password"])
    print("\n")