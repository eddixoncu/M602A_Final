from m602.UserActions import UserMenuActions as Actions

from __future__ import annotations
from abc import ABC, abstractmethod
from typing import Any, Optional

class Handler(ABC):
    """
    The Handler interface declares a method for building the chain of handlers.
    It also declares a method for executing a request.
    """

    @abstractmethod
    def set_next(self, handler: Handler) -> Handler:
        pass

    @abstractmethod
    def handle(self, request) -> Optional[str]:
        pass


class AbstractHandler(Handler):
    """
    The default chaining behavior can be implemented inside a base handler
    class.
    """

    _next_handler: Handler = None

    def set_next(self, handler: Handler) -> Handler:
        self._next_handler = handler
        # Returning a handler from here will let us link handlers in a
        # convenient way like this:
        # monkey.set_next(squirrel).set_next(dog)
        return handler

    @abstractmethod
    def handle(self, request: Any) -> str:
        if self._next_handler:
            return self._next_handler.handle(request)

        return None



class ActionProcessor :
    def __init__(self, option) -> None:
        self.option = option


    def execute(self):

        if self.option == Actions["CREATE"]:
            print("Creating")
        elif self.option == Actions["UPDATE"]:
            print("Updating")
        elif self.option == Actions["READ_ALL"]:
            print("Reading")
        elif self.option == Actions["GENERATE_REPORT"]:
            print("Generating")
        elif self.option == Actions["EXIT"]:
            print("LEAVING")

