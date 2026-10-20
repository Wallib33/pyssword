"""A module for designing menus"""

import os
import subprocess
import textwrap


def menu_clear():
    """Clean terminal function"""
    subprocess.run("cls" if os.name == "nt" else "clear", shell=True, check=False)

def main_menu():
    """Main menu made in string text"""
    menu = """
            ======================================================
                            ==============
                            |  Pyssword  |
                            ==============

            Generate a random password in a simple and fast way.
            Choose the password length and your option:

                (1) -> Numbers only (PIN code)

                (2) -> Alphanumeric (letters and numbers)

                (3) -> Complex (letters, numbers, and symbols)

                (4) -> Custom (proceeds to individual questions)

                (5) -> Exit
            ======================================================
            """
    # For a better visual in terminal
    print(textwrap.dedent(menu))

def password_menu(gen_mode):
    """The password menu in string text"""
    menu = f"""
            ======================================================
                                ==============
                                |  Pyssword  |
                                ==============

            Welcome to the passowrd generator!
            You choose the {gen_mode} type of password.

            Please set the length of your password above(min: 4, max: 50):
            ======================================================
           """
    print(textwrap.dedent(menu))
