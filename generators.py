"""A module that contains de password generators function"""

import string
import time
from random import choice

import menu

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
complex = letters + digits + symbols

def pin_generator():
    generator_mode = "PIN"

    while True:
        menu.menu_clear()
        menu.password_menu(generator_mode)

        try:
            generate_password = " "
            password_length = int(input(":"))

            if password_length < 4:
                print(f"\nThe password length must be greater than {password_length}")
            elif password_length > 50:
                print(f"\nThe password length must be less than {password_length}")
            else:
                print(f"\nGenerating your {generator_mode} password.")

                for c in range(password_length):
                    c = choice(digits)
                    generate_password +=  c

                menu.menu_clear()
                print("\nYour Password generated is:")
                print(f"{generate_password.strip()}")

                while True:
                    print("\nYou want to try again? (y/n)")
                    option = input(":").strip().lower()

                    if option == "y":
                        break
                    elif option == "n":
                        print("\nFinish the PIN Generator mode.")
                        time.sleep(1)
                        return
                    else:
                        print(f"\nOption {option} is not valid, please choose (y or n)")

        except ValueError:
            print("Password Length should be a number (Intenger)!")
            print("Try again.")
            continue

        except KeyboardInterrupt:
            print(" | Force Exit")
            break

def alphanumeric_generator():
    # TODO: The alphanumeric password generator
    pass

def complex_generator():
    # TODO: The complex password generator
    pass

def custom_generator():
    # TODO: The custom password generator
    pass