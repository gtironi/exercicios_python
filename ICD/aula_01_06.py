from bokeh.io import output_file, save, show
from bokeh.models import Range1d
from bokeh.plotting import figure
from sklearn import datasets
import numpy as np

output_file("exemplo4.html")

plot = figure(width=640, height=480, tools="box_zoom, pan, reset, save, wheel_zoom")
plot.toolbar.logo = None
plot.toolbar.autohide = True
plot.toolbar_location = "below"

renderer = plot.circle([1,2,3,4,5], [2,4,6,8,10], legend_label = "sei lá", color = "red")
renderer1 = plot.circle([1,2,3,4,5], [4,6,8,10,12], legend_label = "não sei", color = "blue")
plot.legend.location = "top_left"
plot.legend.background_fill_alpha = 0
plot.legend.border_line_color = None
# plot.legend.padding = 42
plot.legend.label_text_color = "cyan"
plot.legend.label_text_font = "times"

glyph_renderer = renderer.glyph
glyph_renderer.size = 42
glyph_renderer = renderer1.glyph
glyph_renderer.size = 30



show(plot)