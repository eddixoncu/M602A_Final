

from os import system, name
from m602.EmissionsCalculator import EmissionsCalculator
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
    options = Actions.UserMenuActions.values()
    while True :
        option = Actions.show_menu()

        if option == Actions.UserMenuActions["CREATE"]:
            print("Creating")
        elif option == Actions.UserMenuActions["UPDATE"]:
            print("Updating")
        elif option == Actions.UserMenuActions["READ_ALL"]:
            print("Reading")
        elif option == Actions.UserMenuActions["GENERATE_REPORT"]:
            print("Generating")
        elif option == Actions.UserMenuActions["EXIT"]:
            print("LEAVING")
            break

    #clear()
    print("END111")
    

if __name__ == "__main__":
    main()
