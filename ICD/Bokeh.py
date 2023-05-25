from bokeh.plotting import figure
from bokeh.io import output_file, save, show

x = [1,7,13,42]
y = [2, 14, 26, 84]

output_file("line_plot.html")

figure = figure()
figure.line(x, y)
save(figure)


