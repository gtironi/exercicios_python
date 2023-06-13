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

output_file("periodic_table.html")

plot = figure()
plot.xaxis.axis_label = "Atomic Radius"
plot.yaxis.axis_label = "Boiling Point"

plot.circle(x = "atomic radius", y = "boiling point", size = "size", color = "color", fill_alpha = 0.13, legend_label = "gas", source = gas)
plot.circle(x = "atomic radius", y = "boiling point", size = "size", color = "color", fill_alpha = 0.13, legend_label = "liquid", source = liquid)
plot.circle(x = "atomic radius", y = "boiling point", size = "size", color = "color", fill_alpha = 0.13, legend_label = "solid", source = solid)

show(plot)