import string
import random

LENGTH = 16

def generate_password() -> str:
    """
    Generates a safe password.

    Returns:
        str: Generated password
    """
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    special = string.punctuation

    charset = lowercase + uppercase + digits + special

    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(special)
    ]

    for _ in range(0, LENGTH - 4):
        password.append(random.choice(charset))

    random.shuffle(password)

    return "".join(password)

print(generate_password())