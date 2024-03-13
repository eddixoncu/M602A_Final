"""
Main program
"""

from m602.ActionHandler import ActionHandler
import m602.UserActions as Actions


def main():
    """
    Program's main method.
    """
    option = -1
    processor = ActionHandler(Actions.UserMenuActions["EXIT"])

    while True:
        option = Actions.show_main_menu()
        if option == Actions.UserMenuActions["EXIT"]:
            break
        processor.option = option
        processor.execute()

    print("\nEND!!!\n")


if __name__ == "__main__":
    main()
