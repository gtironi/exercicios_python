from bokeh.io import output_file, save, show
from bokeh.models import Range1d
from bokeh.plotting import figure
from sklearn import datasets
import numpy as np

output_file("exemplo4.html")

plot = figure(width=640, height=480, tools="box_zoom, pan, reset, save, wheel_zoom")
plot.toolbar.logo= None
plot.toolbar.autohide = True
plot.toolbar_location = "below"

plot.circle([1,2,3,4,5],[2,4,6,8,10])

show(plot)