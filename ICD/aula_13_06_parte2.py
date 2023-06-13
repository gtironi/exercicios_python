from bokeh.layouts import gridplot
from bokeh.models.annotations import Span, BoxAnnotation
from bokeh.plotting import figure, output_file, show

output_file("grid_plot.html")

x = list(range(0,11))
y = list(range(10,21))

plot1 = figure(width = 240, height=240, title = "Circle Glyphs")
plot1.circle(x,y,size = 13, color = "OrangeRed", alpha = 0.42)

plot2 = figure(width = 240, height=240, title = "Triangle Glyphs")
plot2.triangle(x,y,size = 13, color = "Fuchsia", alpha = 0.42)

plot3 = figure(width = 240, height=240, title = "Square Glyphs")
plot3.square(x,y,size = 13, color = "SeaGreen", alpha = 0.42)

plot = gridplot([[plot1, plot2], [plot3, None]])

show(plot)