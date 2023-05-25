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