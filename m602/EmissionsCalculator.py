"""
Contains classes intended for calculating CO2 emission from different sources.
"""

CONST_ELECTRICITY_BILL = 0.0005
CONST_GAS_BILL = 0.0053
CONST_FUEL_BILL = 2.32
CONST_WASTE = 0.57
CONST_FUEL_EFFICIENCY = 2.31


class EmissionsCalculator:
    """
    Calculator of Kg of CO2 from the three common sources
    """
    def __init__(self):
        pass

    def calculate_energy_emissions(self, electricity_bill, gas_bill, fuel_bill):
        """
        Calculates the yearly emitted CO2 from energy usage of sources such electricity, gas, and fuel.
        :param: electricity_bill: Average monthly electricity bill in euros.
        :param: gas_bill: Average monthly gas bill in euros.
        :param: fuel_bill:Average monthly fuel in euros.
        :return: The emitted amount of kilograms of CO2
        """
        electricity_emission = electricity_bill * 12 * CONST_ELECTRICITY_BILL
        gas_emission = gas_bill * 12 * CONST_GAS_BILL
        fuel_emission = fuel_bill * 12 * CONST_FUEL_BILL
        return electricity_emission + gas_emission + fuel_emission

    def calculate_waste_emissions(self, generated_waste, disposed_wasted):
        """
        Calculates the yearly emitted CO2 from waste
        :param: generated_waste
        :param: disposed_wasted
        :return: The emitted amount of kilograms of CO2
        """
        disposed_wasted /= 100
        waste_emission = generated_waste * 12 * (CONST_WASTE - (disposed_wasted / generated_waste))
        return waste_emission

    def calculate_travel_emissions(self, kilometers_traveled, avg_fuel_efficiency):
        """
        :param: kilometers_traveled: Kilometres traveled per year
        :param: avg_fuel_efficiency: Fuel efficiency measured in liters per 100 Km
        :return: The emitted amount of kilograms of CO2
        """
        travel_emission = kilometers_traveled * (1 / avg_fuel_efficiency) * CONST_FUEL_EFFICIENCY
        return travel_emission
