# from bokeh.io import show, output_file, curdoc
# from bokeh.models import ColumnDataSource
# from bokeh.plotting import figure
# from bokeh.models.widgets import Button
# from bokeh.models.ranges import FactorRange
# from bokeh.layouts import row,column


# fruits = ['Apples', 'Pears', 'Nectarines', 'Plums', 'Grapes', 'Strawberries']
# counts = [5, 3, 4, 2, 4, 6]

# source = ColumnDataSource(data=dict(fruits=fruits, counts=counts))

# p = figure(x_range=fruits, plot_height=350, toolbar_location='left', title="Fruit Counts", tools='wheel_zoom')
# p.vbar(x='fruits', top='counts', width=0.9, source=source, legend_field="fruits",
#        line_color='white', fill_color='dodgerblue')

# p.xgrid.grid_line_color = None
# p.legend.orientation = "horizontal"
# p.legend.location = "top_center"

# def plot_change():
#     fruits = ['Banana', 'Orange']
#     counts = [41, 12]
#     source.data = dict(fruits=fruits, counts=counts)
#     p.x_range.factors = fruits

# button_classify = Button(label="Change Vbar")
# button_classify.on_click(plot_change)

# layout = column(button_classify, p)
# curdoc().add_root(layout)
# curdoc().title = "VBar"

from bokeh.core.enums import Orientation
from bokeh.models.annotations import Title
import pandas as pd
import numpy as np
from bokeh.io import curdoc, output_notebook
from bokeh.models.tools import HoverTool
from bokeh.models import DateRangeSlider,  ColumnDataSource, PreText, Select, Range1d, RadioButtonGroup, Div, CustomJS, Button
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column, row
import random


df = pd.read_csv("./data/country_wise_latest.csv")
ArrBenua = np.array(["All"])
ArrBenua = np.append(ArrBenua,df["WHO Region"].unique())
ArrCountry = np.array(["All"])

ArrCountry = np.append(ArrCountry,df["Country/Region"].unique())
df_Column = np.array(list(df.columns))
df_Column = np.delete(df_Column, [0,-1])

testdf = df['Country/Region'][df["WHO Region"] == "Africa"].values.tolist()
print(testdf)