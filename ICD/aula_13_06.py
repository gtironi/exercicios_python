from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure
from bokeh.sampledata.periodic_table import elements
import pandas as pd

pd.set_option("display.max_columns", None)

'''
print(elements.head())
print(elements.count())
print(elements)
'''

elements.dropna(inplace=True)

color_dict = {"gas":"blue", "liquid":"orange","solid":"grey"}

colors = []

for each_element in elements["standard state"]:
    colors.append(color_dict[each_element])

elements["size"] = elements["van der Waals radius"]/10
elements["color"] = colors

for estado in color_dict.keys():
    globals()[estado] = ColumnDataSource(elements[elements["standard state"] == estado])

