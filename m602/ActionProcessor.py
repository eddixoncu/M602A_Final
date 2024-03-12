from m602.UserActions import UserMenuActions as Actions


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

