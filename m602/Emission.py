import json
from dataclasses import dataclass
from typing import List


@dataclass
class Emission:
    """
    Define a record of Kg of CO2 for the given year
    """
    total_kg: float
    year: int
    kind: str

    def __init__(self, year, total_kg, kind):
        self.total_kg = total_kg
        self.year = year
        self.kind = kind


@dataclass
class Emissions:
    """
    Define a store of emissions.
    """
    emissions: List[Emission]

    def __post_init__(self):
        self.emissions = [Emission(**emission) for emission in self.emissions]


"""
def _load_store(file="store.json"):
    f = open(file)

    # returns JSON object as
    # a dictionary
    data = json.load(f)
    print(len(data))
    if (len(data) > 0):
        print(len(data["emissions"]))
    # Iterating through the json
    # list
    for em in data['emissions']:
        print(em)

    # Closing file
    f.close()

    records = Emissions(**data)
    return records.emissions


info = _load_store()
print(type(info))
for inf in info:
    print(type(inf))
    print(inf)


# Opening JSON file

files = ["data.json", "data0.json", "data_empty.json", "no_exist_data.json"]
i = 0
tam = len(files)
while i < tam:
    try:
        file = files[i]
        if file == "data_empty.json":
            open(file, 'w').close()
            #f = open(file, 'r+')
            #f.truncate(0)
            #f.close()

            print("Truncating data for ", file)

        print(f"\nOpening {file}")

        f = open(file)

        # returns JSON object as
        # a dictionary
        data = json.load(f)
        print(len(data))
        if (len(data) > 0 ):
            print(len(data["emissions"]))
        # Iterating through the json
        # list
        for em in data['emissions']:
            print(em)

        # Closing file
        f.close()

        records = Emissions(**data)

        print(records)
        i += 1
    except Exception as ex:
        print(f"JSON object issue: {ex}")
        i += 1
        continue
"""
