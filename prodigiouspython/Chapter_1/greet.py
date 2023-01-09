"""Module to greet the user"""

import getpass


def hello():
    """Greets the user."""
    username: str = getpass.getuser().capitalize()
    print(f"Hello {username}. Have a great day :)")


if __name__ == "__main__":
    hello()
