import string
from typing import Tuple

LENGTH = 16

def check_password(password: str) -> Tuple[bool, str]:
    """
    Checks a password if it matches the following constraints:
        - Length
        - Upper/Lowercase characters
        - Digits
        - Special characters

    Args:
        password (str): Password to validate

    Returns:
        Tuple[bool, str]: Returns validation indicator and a reason
    """

    if len(password) < LENGTH:
        return False, f"Das Passwort muss mindestens {LENGTH} Zeichen lang sein."

    if not any(char in password for char in string.ascii_lowercase):
        return False, f"Das Passwort muss Kleinbuchstaben beinhalten."

    if not any(char in password for char in string.ascii_uppercase):
        return False, f"Das Passwort muss Großbuchstaben beinhalten."
    
    if not any(char in password for char in string.digits):
        return False, f"Das Passwort muss Zahlen beinhalten."
    
    if not any(char in password for char in string.punctuation):
        return False, f"Das Passwort muss Sonderzeichen beinhalten."

    return True, "Das Passwort ist sicher!"
