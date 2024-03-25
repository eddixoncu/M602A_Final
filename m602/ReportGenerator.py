"""
Module that generates reports
"""

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime

from m602.Emission import Emission


class ChartGenerator:
    """
    Defines a bar chart report generator.
    Based on:
    https://matplotlib.org/stable/gallery/lines_bars_and_markers/barchart.html#sphx-glr-gallery-lines-bars-and-markers-barchart-py
    data from https://allisonhorst.github.io/palmerpenguins/
    """
    categories: ()
    data: {}
    title: str
    y_label: str
    output_file: str

    def __init__(self, categories, data, title, y_label):
        self.categories = categories
        self.data = data
        self.title = title
        self.y_label = y_label

    def build_report(self):
        x = np.arange((len(self.categories)))
        width = 0.125  # the width of the bars
        multiplier = 0
        fig, ax = plt.subplots(layout='constrained')

        for attribute, measurement in self.data.items():
            offset = width * multiplier
            rects = ax.bar(x + offset, measurement, width, label=attribute)
            ax.bar_label(rects, padding=3)
            multiplier += 1

        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel(self.y_label)  # y label
        ax.set_title(self.title)  # Title
        ax.set_xticks(x + width, self.categories)
        ax.legend(loc='upper left', ncols=2)
        maximum = self._get_max_data()
        maximum = maximum + (30 - (maximum % 30))
        ax.set_ylim(0, maximum)
        now = datetime.now()
        date_string = now.strftime("%Y%m%d_%H%M%S")
        self.output_file = f"chart_{date_string}.pdf"
        plt.savefig(self.output_file, format="pdf", bbox_inches="tight")
        plt.show()

        # plt.close()

    def _get_max_data(self):
        maximum = 0
        for _tuple in self.data.items():

            temp_max = max(_tuple[1])
            if temp_max > maximum:
                maximum = temp_max
        return maximum

    def generate_co2_report(self, emissions: [Emission]):
        measurements_x_year = {}  # year:(e,w,t,T)
        for em in emissions:
            print(f"{em.year}: {em.total_kg}, {em.energy_emission} + {em.waste_emission} + {em.travel_emission}")

        energy = tuple(e.energy_emission for e in emissions)
        waste = tuple(e.waste_emission for e in emissions)
        travel = tuple(e.travel_emission for e in emissions)
        total = tuple(e.total_kg for e in emissions)
        years = tuple(e.year for e in emissions)
        print(years)
        print(energy)
        print(waste)
        print(travel)
        print(total)
        measurements_x_year["Energy"] = energy
        measurements_x_year["Waste"] = waste
        measurements_x_year["Travel"] = travel
        measurements_x_year["Total"] = total

        self.categories = years
        self.data = measurements_x_year
        self.title = "Emissions of CO2"
        self.y_label = "Kg CO2"
        self.build_report()

""" 
# USAGE
species = ("Adelie", "Chinstrap", "Gentoo", "Others")  # categories
penguin_means = {  # data
    'Bill Depth': (18.35, 18.43, 14.98, 13),
    'Bill Length': (38.79, 48.83, 47.50, 50),
    'Flipper Length': (189.95, 195.82, 217.19, 150),
    'Feat': (95, 82, 19, 75)
}

gntor = ChartGenerator(species, penguin_means, 'Pingüinos X especie', 'longitud(mm)')
gntor.build_report()
"""

"""
species = ("Adelie", "Chinstrap", "Gentoo", "other")  # categories
penguin_means = {  # data
    'Bill Depth': (18.35, 18.43, 14.98, 13),
    'Bill Length': (38.79, 48.83, 47.50, 50),
    'Flipper Length': (189.95, 195.82, 217.19, 150),
    'Feat': (95, 82, 19, 75)
}

x = np.arange(len(species))  # the label locations
width = 0.125  # the width of the bars
multiplier = 0

fig, ax = plt.subplots(layout='constrained')

for attribute, measurement in penguin_means.items():
    offset = width * multiplier
    rects = ax.bar(x + offset, measurement, width, label=attribute)
    ax.bar_label(rects, padding=3)
    multiplier += 1

# Add some text for labels, title and custom x-axis tick labels, etc.
ax.set_ylabel('Length (mm)')  # y label
ax.set_title('Penguin attributes by species')  # Title
ax.set_xticks(x + width, species)
ax.legend(loc='upper left', ncols=3)
ax.set_ylim(0, 250)

now = datetime.now()
date_string = now.strftime("%Y%m%d_%H%M%S")
output_file = f"chart_{date_string}.pdf"
plt.savefig(output_file, format="pdf", bbox_inches="tight")
plt.show()

# plt.close()
"""
