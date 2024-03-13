"""
Contains general purpose constants and functions
"""
from os import system, name

UserMenuActions = {
    "EXIT": 0,
    "CREATE": 1,
    "UPDATE": 2,
    "READ_ALL": 3,
    "GENERATE_REPORT": 4,
    "CLEAR": 5,
}

EmissionType = {
    "ENERGY": 1,
    "WASTE": 2,
    "TRAVEL": 3,
}


def show_main_menu():
    """
    Displays a set of options for the menu.
    :return: The user's choice.
    """
    print("Please enter the action you want to perform, or press any key to exit")
    print("[1]\tCREATE RECORD")
    print("[2]\tUPDATE RECORD")
    print("[3]\tSEE ALL DATA")
    print("[4]\tGENERATE REPORT")
    print("[5]\tCLEAR SCREEN")

    option = input("\n>> ")
    return validate_input(option)


def validate_input(data):
    """
    Validates if data is a valid integer option value
    :param data: Option to be validated.
    :return: If input is valid option,  it will return the correspondent key or zero i.o.c
    """
    options = UserMenuActions.values()
    value = 0
    try:
        value = int(data)
        if value not in options:
            value = 0

    except ValueError:
        value = 0
    return value


def show_emission_options():
    """
    Displays a set of options for the type of emissions menu.
    :return: The user's choice.
    """
    try:
        print("What kind of CO2 emission do you want to calculate? ")
        print("[1]\tEnergy")
        print("[2]\tWaste")
        print("[3]\tTravel")
        emission_type = int(input(">> "))
        return emission_type

    except ValueError:
        return 0


def clear():
    """
    Check and make call clear command for specific operating system
    """
    if name == 'nt':
        _ = system('cls')

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
