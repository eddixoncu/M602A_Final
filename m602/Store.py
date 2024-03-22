"""
Defines classes and functions intended for manage a based sqlite store.
"""
import sqlite3
from m602.Emission import Emission


class Store:
    """
    Define a  based sqlite storage.
    """

    def __init__(self, data=None, path="store.db"):
        if data is None:
            data = []
        self.data = data
        self.path = path

    def get_all(self):
        """
        Returns all recorded emissions
        :return: Stored emissions ordered by year.
        """
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                cursor.execute("""SELECT year, total_kg, energy_emission, waste_emission, travel_emission FROM emission 
                               ORDER BY year""")
                output = cursor.fetchall()
                for row in output:  # row is a tuple
                    e = Emission(row[0], row[2], row[3], row[4])
                    self.data.append(e)

            return self.data

        except Exception as exc:
            print(f"ISSUE on get_all: {exc}")
            # traceback.print_exc()
            return []

    def exists_emission_by_year(self, year):
        """
        Checks if exist a record emission for the given year.
        :param year: Year to be checked.
        :return: True if exists, false if it doesn't
        """
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                cursor.execute("SELECT COUNT(*) FROM emission WHERE year = ?", (year,))
                count = cursor.fetchall()  # tuples array
                exists = count[0][0]
                return exists != 0
        except Exception as exc:
            print(f"ISSUE on exists: {exc}")

    def add_record(self, record: Emission):
        """
        Inserts into the database a new record of emission.
        :param record: Emission object to be stored.
        """
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                cursor.execute(""" INSERT INTO emission (year, energy_emission, waste_emission, travel_emission, 
                                        total_kg) VALUES (?,?,?,?,?) """,
                               (record.year, record.energy_emission, record.waste_emission, record.travel_emission,
                                record.total_kg))
        except Exception as exc:
            print(f"ISSUE on add_record: {exc}")

    def update_record(self, record: Emission):
        """
        Updates the record of emission.
        :param record: Emission object to be updated.
        """
        try:
            with sqlite3.connect(self.path) as conn:
                cursor = conn.cursor()
                cursor.execute(""" UPDATE emission SET energy_emission=?, waste_emission=?, travel_emission=?, 
                                        total_kg=? WHERE year=? """,
                               (record.energy_emission, record.waste_emission, record.travel_emission, record.total_kg,
                                record.year))
        except Exception as exc:
            print(f"ISSUE on update record: {exc}")
