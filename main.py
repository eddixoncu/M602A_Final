from os import system, name
from m602.ActionProcessor import ActionProcessor
import m602.UserActions as Actions


def clear():
    """
    Check and make call clear command for specific operating system
    """
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')


def main():
    """
    Main program
    """
    option = -1
    processor = ActionProcessor (Actions.UserMenuActions["EXIT"])

    while True:
        option = Actions.show_main_menu()
        if option == Actions.UserMenuActions["EXIT"]:
            break
        processor.option = option
        processor.execute()

    clear()
    print("\nEND!!!")


if __name__ == "__main__":
    main()
