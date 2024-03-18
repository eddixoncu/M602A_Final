"""
Defines classes and functions intended for manage a based file store.
"""
import json
import os
import traceback

from m602.Emission import Emissions


class Store:
    """
    Define a  based JSON file storage.
    """

    def __init__(self, data=None, path="store.json"):
        if data is None:
            data = []
        self.data = data
        self.path = path

    def delete_storage(self):
        if os.path.exists(self.path):
            os.remove(self.path)

    def load_store(self):
        try:
            f = None
            print(f"Reading store from {os.path.abspath(self.path)}")
            if os.path.exists(self.path):
                f = open(self.path)
            else:
                f = open(self.path, 'w')

            #str_json = f.read()
            #lines = f.readlines()
            num_lines = 1 # len(lines)
            if num_lines == 0:
                pass
                #self.data = []

            else:
                # returns JSON object as
                # a dictionary

                data = json.load(f)

                # Closing file
                records = Emissions(**data)
                self.data = records.emissions

            f.close()
            return self.data
        except Exception as exc:
            print(f"ISSUE: {exc}")
            # traceback.print_exc()
            return []

    def add_record(self, record):
        self.data.append(record)
        # emissions = Emissions()
