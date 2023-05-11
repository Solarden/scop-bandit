import secrets
import string


def generate_identifier(length: int = 8) -> str:
    # Generate a random string of the specified length using the secrets module
    identifier: str = "".join(secrets.choice(string.ascii_letters + string.digits) for _ in range(length))
    # Return the identifier
    return identifier
