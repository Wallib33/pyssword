""" A Python Password Generator """

import time

import menu
from generators import (
    alphanumeric_generator,
    complex_generator,
    custom_generator,
    pin_generator,
)

"""The main function wheres the programs start"""
def main():
    while True:
        menu.menu_clear()
        menu.main_menu()

        try:
            option = int(input(":"))

            if option == 1:
                pin_generator()
                continue
            elif option == 2:
                alphanumeric_generator()
                continue
            elif option == 3:
                complex_generator()
                continue
            elif option == 4:
                custom_generator()
                print("\nIn development...")
                time.sleep(2)
                continue
            elif option == 5:
                print("Leaving de Pyssword!")
                break
            else:
                print(f"\n{option} Is not a option in menu!")
                print("Select a option in menu")
                time.sleep(2)
                continue
        except ValueError:
            print("The option should be a number(Integer)!")
            print("Try again")
            time.sleep(2)
            continue
        except KeyboardInterrupt:
            print(" | Force exit")

    print("\nEnd of script!")

if __name__ == "__main__":
    main()
