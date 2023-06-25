from bokeh.io import output_file, show
from bokeh.models import ColumnDataSource
from bokeh.plotting import figure

output_file("exemplo5.html")

raw_data = {'x':[1,2,3,4,5], 'y':[2,4,6,8,10]}

data_source = ColumnDataSource(data=raw_data)

plot = figure()

new_data = [3,6,9,12,15]

data_source.data["z"] = new_data

data_source.patch({'x':[(0,10)]})

plot.circle(x ="x", y="z", source = data_source)

show(plot)