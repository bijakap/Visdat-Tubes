from re import template
from bokeh.models.annotations import Title
import pandas as pd
import numpy as np
from bokeh.io import curdoc, output_notebook
from bokeh.models.tools import HoverTool
from bokeh.models import DateRangeSlider,  ColumnDataSource, PreText, Select, Range1d, RadioButtonGroup, Div, CustomJS, Button
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column, row
import random

#inisiasi Data
df = pd.read_csv("./data/country_wise_latest.csv")
ArrBenua = df["WHO Region"].unique()
ArrBenua = np.append(ArrBenua,"All")
ArrCountry = df["Country/Region"].unique()
ArrCountry = np.append(ArrCountry,"All")
df_Column = np.array(list(df.columns))
df_Column = np.delete(df_Column, [0,-1])

# Default value
case = "Confirmed"
region = 'All'
country = 'All'
theme = 'dark_minimal'

#sidebar dropdown
region_select = Select(value=region, title='Region', options=list(ArrBenua), name="region_select")
country_select = Select(value=country, title='Country', options=list(ArrCountry), name="country_select")
colums_select = Select(value=case, title='Case', options=list(df_Column ), name="case_select")

#def fungsi
def Handle_Change_Region(attrname, old, new):
    if region_select.value == "All":
        country_select.options = list(ArrCountry)
    else :
        newCountryList = df['Country/Region'][df["WHO Region"] == region_select.value].to_numpy()
        country_select.options = list(newCountryList)

    

region_select.on_change('value',Handle_Change_Region)

#init figure kosong
testdf = df
ds = ColumnDataSource(testdf)
data = dict(x = ds.data['Country/Region'], y = ds.data['Confirmed'])
TOOLTIPS = [
    ("Nama", "@x"),
    ("Number", "@y"),
]
plt = figure(x_range=data['x'], y_range=(0,100000), height=250 ,title="Percobaan All", sizing_mode="stretch_both", tooltips=TOOLTIPS)
plt.vbar(x='x', top='y', width=0.9, source=data)
plt.y_range.start = 0
plt.xgrid.grid_line_color = None
plt.xaxis.major_label_orientation = "vertical"
show(plt)

# Layouting
about_text = """
    <style>
        .name {
            border: 2px solid red;
            border-radius: 10px;
            width:100%;
        }
    </style>
    <div>
        <ul class="name">
            <li>Yantrisnandra Akbar Maulino</li>
            <li>Reyhan Septri Asta</li>
            <li>Bijak Algifan Putra</li>
        </ul>
    </div>
"""
about = Div(text=about_text, width_policy="max")
controls = column(row(region_select, country_select, sizing_mode="stretch_width"), colums_select, about)
main_layout = column(row(controls, plt),sizing_mode="stretch_both")
curdoc().add_root(main_layout)
curdoc().title = "Tubes Visdat Boy"
curdoc().theme = theme