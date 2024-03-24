"""
Module that generates reports
"""

import matplotlib.pyplot as plt
import numpy as np
from datetime import datetime


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
        ax.set_ylabel('Length (mm)')  # y label
        ax.set_title('Penguin attributes by species')  # Title
        ax.set_xticks(x + width, self.categories)
        ax.legend(loc='upper left', ncols=3)
        ax.set_ylim(0, 350)
        now = datetime.now()
        date_string = now.strftime("%Y%m%d_%H%M%S")
        output_file = f"chart_{date_string}.pdf"
        plt.savefig(output_file, format="pdf", bbox_inches="tight")
        plt.show()

        # plt.close()


species = ("Adelie", "Chinstrap", "Gentoo", "other")  # categories
penguin_means = {  # data
    'Bill Depth': (18.35, 18.43, 14.98, 13),
    'Bill Length': (38.79, 48.83, 47.50, 50),
    'Flipper Length': (189.95, 195.82, 217.19, 150),
    'Feat': (95, 82, 19, 75)
}

gntor = ChartGenerator(species, penguin_means, 'Penguin attributes by species', 'Length (mm)')
gntor.build_report()

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
