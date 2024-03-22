"""
Contains model classes
"""


class Emission:
    """
    Define a record of Kg of CO2 for the given year
    """
    total_kg: float
    year: int
    kind: str
    energy_emission: float
    waste_emission: float
    travel_emission: float

    def __init__(self, year, energy_emission=0, waste_emission=0, travel_emission=0):
        self.total_kg = energy_emission + waste_emission + travel_emission
        self.year = year
        self.energy_emission = energy_emission
        self.waste_emission = waste_emission
        self.travel_emission = travel_emission
