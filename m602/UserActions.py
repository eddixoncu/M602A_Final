"""
Contains general purpose constants and functions
"""
from os import system, name

from m602.Emission import Emission
from m602.EmissionsCalculator import EmissionsCalculator

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

calculator = EmissionsCalculator()


def show_main_menu():
    """
    Displays a set of options for the menu.
    :return: The user's choice.
    """
    print("\nPlease choose and option to perform and then press ENTER")
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


def get_emission_by_energy_from_input(year):
    """
    Obtains an emission by energy usage from object the user input
    :param year: year to be recorded
    :return: An object of emission
    """
    electricity_bill = float(input("Enter the average monthly electricity bill: "))
    gas_bill = float(input("Enter the average monthly gas bill: "))
    fuel_bill = float(input("Enter the average monthly fuel bill: "))
    total_energy_emission = calculator.calculate_energy_emissions(electricity_bill, gas_bill, fuel_bill)
    return Emission(year, total_energy_emission, "ENERGY")


def get_emission_by_waste_from_input(year):
    """
    Obtains an emission by generated waste object from the user input
    :param year: year to be recorded.
    :return: An object of emission
    """
    generated_waste = float(input("Enter the average of generated wasted in Kg: "))
    percentage = float(input("Enter the percentage of recycled/composted waste (0-100)%"))
    total_waste_emission = calculator.calculate_waste_emissions(generated_waste, percentage)
    return Emission(year, total_waste_emission, "WASTE")


def get_emission_by_travel_from_input(year):
    """
    Obtains an emission by travel object from the user input
    :param year: year to be recorded.
    :return: An object of emission
    """
    kilometers_traveled = float(input("Enter the kilometres traveled by your employees: "))
    avg_fuel_efficiency = float(input("Enter the fuel efficiency in liters per 100 Km: "))
    travel_emission = calculator.calculate_travel_emissions(kilometers_traveled, avg_fuel_efficiency)
    return Emission(year, travel_emission, "TRAVEL")
