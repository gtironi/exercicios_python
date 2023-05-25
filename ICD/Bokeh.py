from bokeh.plotting import figure
from bokeh.io import output_file, save, show
from sklearn import datasets
import numpy as np

iris = datasets.load_iris()
x = iris.data[:, 2:3]
y = iris.data[:, 3:4]

x_flat = list(np.concatenate(x))
y_flat = list(np.concatenate(y))

output_file("iris.html")

figure = figure()
figure.circle(x_flat, y_flat)
figure.background_fill_color = "#0000ff"
figure.background_fill_alpha = 0.3

# figure.plot_width = 1280
# figure.plot_height = 720

show(figure)