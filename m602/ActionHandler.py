"""
Contains classes intended for managing the user's request.
"""

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

from m602.ReportGenerator import ChartGenerator
from m602.UserActions import UserMenuActions as Actions, EmissionType
from m602.UserActions import show_emission_options
from m602.UserActions import (get_emission_by_energy_from_input,
                              get_emission_by_waste_from_input,
                              get_emission_by_travel_from_input,
                              clear)
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


class CreateOrUpdateHandler(AbstractHandler):
    def handle(self, request):
        if request == Actions["CREATE"]:
            print("Creating from handler")
            emission_type = show_emission_options()
            if emission_type == 0:
                return

            year = int(input("Enter the year to be calculated: \n"))
            emission = None
            if emission_type == EmissionType["ENERGY"]:
                emission = get_emission_by_energy_from_input(year)
            elif emission_type == EmissionType["WASTE"]:
                emission = get_emission_by_waste_from_input(year)
            elif emission_type == EmissionType["TRAVEL"]:
                emission = get_emission_by_travel_from_input(year)

            emission.total_kg = emission.energy_emission + emission.waste_emission + emission.travel_emission

            exists = super()._store.exists_emission_by_year(year)
            if exists:
                super()._store.update_record(emission)
            else:
                super()._store.add_record(emission)

            print("Emission created ", emission)
        else:
            super().handle(request)


class ClearHandler(AbstractHandler):
    def handle(self, request):
        if request == Actions["CLEAR"]:
            print("Clearing from handler")
            clear()

        else:
            super().handle(request)


class GetAllHandler(AbstractHandler):
    def handle(self, request):
        if request == Actions["READ_ALL"]:
            print("Getting all from handler")

            records = super()._store.get_all()  # AbstractHandler._store.load_store() #
            idx = 1
            for r in records:
                print(f"{idx}:\t{r.year}\t{r.total_kg}\t{r.energy_emission}\t{r.waste_emission}\t{r.travel_emission}")
                idx += 1
        else:
            super().handle(request)


class GenerateReportHandler(AbstractHandler):
    def handle(self, request):
        if request == Actions["GENERATE_REPORT"]:
            print("Generating from handler")

            emissions = super()._store.get_all()
            report_gen = ChartGenerator((),{}, "Emissions of CO2 per year", "Kg" )
            report_gen.generate_co2_report(emissions)

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
        create_update_handler = CreateOrUpdateHandler()
        get_all_data_handler = GetAllHandler()
        generate_resport_handler = GenerateReportHandler()
        clear_handler = ClearHandler()

        create_update_handler.set_next(generate_resport_handler).set_next(get_all_data_handler).set_next(clear_handler)

        create_update_handler.handle(self.option)
