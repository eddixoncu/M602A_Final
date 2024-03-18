"""
Contains classes intended for managing the user's request.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional
from m602.UserActions import UserMenuActions as Actions, EmissionType
from m602.UserActions import show_emission_options
from m602.EmissionsCalculator import EmissionsCalculator
from m602.Emission import Emission
from m602.Store import Store


class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        """
        Abstract method that sets a new handler to the chain.
        :param handler: Handler to be added.
        """
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        """
        Abstract method tha handles the user's request.
        :param request: Request to be processed.
        """
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None
    _store: Store = Store()

    def set_next(self, handler: Handler) -> Handler:
        """
        Returning a handler from here will let us link handlers in a convenient way like this:
        handler_1.set_next(handler_2).set_next(handler_3)....set(handler_n)
        :param handler: Handler to be added to the chain
        :return: The added handler.
        """
        self._next_handler = handler

        return handler

    @abstractmethod
    def handle(self, request: Any) -> str | None:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None


class CreateHandler(AbstractHandler):
    def handle(self, request):
        if request == Actions["CREATE"]:
            print("Creating from handler")
            emission_type = show_emission_options()
            if emission_type == 0:
                return

            year = int(input("Enter the year to be calculated: \n"))
            calculator = EmissionsCalculator()
            emission = None
            if emission_type == EmissionType["ENERGY"]:
                electricity_bill = float(input("Enter the average monthly electricity bill: "))
                gas_bill = float(input("Enter the average monthly gas bill: "))
                fuel_bill = float(input("Enter the average monthly fuel bill: "))
                total_energy_emission = calculator.calculate_energy_emissions(electricity_bill, gas_bill, fuel_bill)
                emission = Emission(year, total_energy_emission)
            elif emission_type == EmissionType["WASTE"]:
                generated_waste = float(input("Enter the average of generated wasted in Kg: "))
                percentage = float(input("Enter the percentage of recycled/composted waste (0-100)%"))
                total_waste_emission = calculator.calculate_waste_emissions(generated_waste, percentage)
                emission = Emission(year, total_waste_emission)
            elif emission_type == EmissionType["TRAVEL"]:
                kilometers_traveled = float(input("Enter the kilometres traveled by your employees: "))
                avg_fuel_efficiency = float(input("Enter the fuel efficiency in liters per 100 Km: "))
                travel_emission = calculator.calculate_travel_emissions(kilometers_traveled, avg_fuel_efficiency)
                emission = Emission(year, travel_emission)
        else:
            super().handle(request)


class UpdateHandler(AbstractHandler):
    def handle(self, request):
        if request == Actions["UPDATE"]:
            print("Updating from handler")
            emission_type = show_emission_options()
            if emission_type == 0:
                return

            year = int(input("Enter the year to be calculated: \n"))
            calculator = EmissionsCalculator()
            emission = None
            if emission_type == EmissionType["ENERGY"]:
                electricity_bill = float(input("Enter the average monthly electricity bill: "))
                gas_bill = float(input("Enter the average monthly gas bill: "))
                fuel_bill = float(input("Enter the average monthly fuel bill: "))
                total_energy_emission = calculator.calculate_energy_emissions(electricity_bill, gas_bill, fuel_bill)
                emission = Emission(year, total_energy_emission)
            elif emission_type == EmissionType["WASTE"]:
                generated_waste = float(input("Enter the average of generated wasted in Kg: "))
                percentage = float(input("Enter the percentage of recycled/composted waste (0-100)%"))
                total_waste_emission = calculator.calculate_waste_emissions(generated_waste, percentage)
                emission = Emission(year, total_waste_emission)
            elif emission_type == EmissionType["TRAVEL"]:
                kilometers_traveled = float(input("Enter the kilometres traveled by your employees: "))
                avg_fuel_efficiency = float(input("Enter the fuel efficiency in liters per 100 Km: "))
                travel_emission = calculator.calculate_travel_emissions(kilometers_traveled, avg_fuel_efficiency)
                emission = Emission(year, travel_emission)
        else:
            super().handle(request)


class GetAllHandler(AbstractHandler):
    def handle(self, request):
        if request == Actions["READ_ALL"]:
            print("Getting all from handler")

            records = super()._store.load_store()  # AbstractHandler._store.load_store() #
            idx = 1
            for r in records:
                print(f"{idx}:\t{r.year}\t{r.kind}\t{r.total_kg}")
                idx += 1
        else:
            super().handle(request)


class GenerateReportHandler(AbstractHandler):
    def handle(self, request):
        if request == Actions["GENERATE_REPORT"]:
            print("Generating from handler")
        else:
            super().handle(request)


class ActionHandler:
    """
    Class the manage the user's choice.
    """

    def __init__(self, option) -> None:
        self.option = option

    def execute(self):
        """
        Executes the user's choice with a chain of handlers.
        """
        create_handler = CreateHandler()
        update_handler = UpdateHandler()
        get_all_data_handler = GetAllHandler()
        generate_resport_handler = GenerateReportHandler()

        create_handler.set_next(update_handler).set_next(generate_resport_handler).set_next(get_all_data_handler)

        create_handler.handle(self.option)
