import pandas as pd
import numpy as np
from bokeh.io import curdoc, output_notebook
from bokeh.models.tools import HoverTool
from bokeh.models import DateRangeSlider,  ColumnDataSource, PreText, Select, Range1d, RadioButtonGroup, Div, CustomJS, Button
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column, row

#inisiasi Data
df = pd.read_csv("./data/country_wise_latest.csv")
ArrBenua = df["WHO Region"].unique()
ArrBenua = np.append(ArrBenua,"All")
ArrCountry = df["Country/Region"].unique()
df_Column = np.array(list(df.columns))
df_Column = np.delete(df_Column, -1)

# Default value
stats = PreText(text='', width=500)
case = "confirmed"
region = 'All'
country = 'Afghanistan'
# source = create_source(region, case)
# total_data = len(source.data['date'])-1
# case_date = pd.to_datetime(source.data['date'])
# slider_value = case_date[0], case_date[-1]
theme = 'dark_minimal'

region_select = Select(value=region, title='Region', options=list(ArrBenua), name="region_select")
country_select = Select(value=country, title='Country', options=list(ArrCountry), name="country_select")
colums_select = Select(value=case, title='Case', options=list(df_Column ), name="case_select")


# Layouting
about_text = """
    <div style="width:300px;">
        <ul class="list-group">
            <li class="list-group-item">Anvaqta Tangguh Wisesa</li>
            <li class="list-group-item">Rachma Indira</li>
            <li class="list-group-item">Rachmansyah Adhi Widhianto</li>
        </ul>
    </div>
"""
about = Div(text=about_text, width_policy="max")
controls = column(row(region_select, country_select), colums_select)
main_layout = column(row(controls, sizing_mode="stretch_height"), sizing_mode="stretch_both")
curdoc().add_root(main_layout)
curdoc().title = "Covid-19 case"
curdoc().theme = theme