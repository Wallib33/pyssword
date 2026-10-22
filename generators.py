"""A module that contains de password generators function"""

import string
import time
from random import choice

import menu

"""Variables for characters types

    Using the string module for capture letters, digits and symbols.

    ascci_letters = Lowercase and Uppercase words.
    digits = Intengers numbers
    ponctuantion = Specials Caracters

"""

letters = string.ascii_letters
digits = string.digits
symbols = string.punctuation
alphanumeric = letters + digits
complex = letters + digits + symbols

def pin_generator():
    # Using for a better GUI.
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
                time.sleep(1) # Added a slowdown for read.

                """Generator with only digits characters"""
                for c in range(password_length):
                    c = choice(digits)
                    generate_password +=  c

                menu.menu_clear()
                print("Your Password generated is:")
                print(f"{generate_password.strip()}")

                while True:
                    print("\nYou want to try again? (y/n)")
                    option = input(":").strip().lower()

                    if option == "y":
                        break
                    elif option == "n":
                        print(f"\nFinishing the {generator_mode} Generator mode.")
                        time.sleep(1)
                        return
                    else:
                        print(f"\nOption {option} is not valid, please choose (y or n)")

        except ValueError:
            print("Password length should be a number (Intenger)!")
            print("Try again.")
            continue

        except KeyboardInterrupt:
            print(" | Force Exit")
            break

def alphanumeric_generator():
    # Using for a better GUI.
    generator_mode = "Alphanumeric"

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
                print(f"\nGenerating your {generator_mode.lower()} password.")
                time.sleep(1) # Added a slowdown for read.

                """Generator with only digits characters"""
                for c in range(password_length):
                    c = choice(alphanumeric)
                    generate_password +=  c

                menu.menu_clear()
                print("Your Password generated is:")
                print(f"{generate_password.strip()}")

                while True:
                    print("\nYou want to try again? (y/n)")
                    option = input(":").strip().lower()

                    if option == "y":
                        break
                    elif option == "n":
                        print(f"\nFinishing the {generator_mode} Generator mode.")
                        time.sleep(1)
                        return
                    else:
                        print(f"\nOption {option} is not valid, please choose (y or n)")

        except ValueError:
            print("Password length should be a number (Intenger)!")
            print("Try again.")
            continue

        except KeyboardInterrupt:
            print(" | Force Exit")
            break

def complex_generator():
    # Using for a better GUI.
    generator_mode = "Complex"

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
                print(f"\nGenerating your {generator_mode.lower()} password.")
                time.sleep(1) # Added a slowdown for read.

                """Generator with only digits characters"""
                for c in range(password_length):
                    c = choice(complex)
                    generate_password +=  c

                menu.menu_clear()
                print("Your Password generated is:")
                print(f"{generate_password.strip()}")

                while True:
                    print("\nYou want to try again? (y/n)")
                    option = input(":").strip().lower()

                    if option == "y":
                        break
                    elif option == "n":
                        print(f"\nFinishing the {generator_mode} Generator mode.")
                        time.sleep(1)
                        return
                    else:
                        print(f"\nOption {option} is not valid, please choose (y or n)")

        except ValueError:
            print("Password length should be a number (Intenger)!")
            print("Try again.")
            continue

        except KeyboardInterrupt:
            print(" | Force Exit")
            break

def custom_generator():
    # TODO: The custom password generator
    pass
