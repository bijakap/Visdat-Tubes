import pandas as pd
from bokeh.io import curdoc, output_notebook
from bokeh.models.tools import HoverTool
from bokeh.models import DateRangeSlider,  ColumnDataSource, PreText, Select, Range1d, RadioButtonGroup, Div, CustomJS, Button
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column, row


df = pd.read_csv("./data/country_wise_latest.csv")
print(df)