from bokeh.core.enums import Orientation
from bokeh.models.annotations import Title
import pandas as pd
import numpy as np
from bokeh.io import curdoc, output_notebook
from bokeh.models import ColumnDataSource, Select, Range1d, Div
from bokeh.plotting import figure, output_file, show
from bokeh.layouts import column, row
import random

#inisiasi Data
df = pd.read_csv("./data/country_wise_latest.csv")
ArrBenua = np.array(["All"])
ArrBenua = np.append(ArrBenua,df["WHO Region"].unique())
ArrCountry = np.array(["All"])
ArrCountry = np.append(ArrCountry,df["Country/Region"].unique())
df_Column = np.array(list(df.columns))
df_Column = np.delete(df_Column, [0,-1])

# Default value
case = "Confirmed"
region = 'All'
country = 'All'
theme = 'dark_minimal'
data = {
    "x" : df["Country/Region"].values.tolist(),
    "y" : df[case].values.tolist()
}
ds = ColumnDataSource(data)

#sidebar dropdown
region_select = Select(value=region, title='Region', options=list(ArrBenua), name="region_select")
country_select = Select(value=country, title='Country', options=list(ArrCountry), name="country_select")
colums_select = Select(value=case, title='Case', options=list(df_Column ), name="case_select")

#def fungsi
def Handle_Change_Dropdown(attrname, old, new):
    print(region_select.value, country_select.value, colums_select.value)
    if region_select.value == "All":
        country_select.options = list(ArrCountry)
    else :
        newCountryList = np.array(["All"])
        newCountryList = np.append(newCountryList,df['Country/Region'][df["WHO Region"] == region_select.value].to_numpy())
        country_select.options = list(newCountryList)
    
    update_plot(region_select.value, country_select.value, colums_select.value)

def update_plot(region, country, case):
    #Bawaan Global
    global ds, plt

    temp = df
    if region != "All":
        print("1")
        temp = df.loc[df["WHO Region"] == region]
        print(temp)
    
    if country != "All":
        print("2")
        temp = df.loc[df['Country/Region'] == country]
        print(temp)

    data = {
        "x" : temp['Country/Region'].values.tolist(),
        "y" : temp[case].values.tolist()
    }
    ds.data.update(data)
    plt.x_range.factors = data['x']
    plt.y_range = Range1d(0, 1000, bounds=(0, None))
    plt.title.text = "Percobaan Ganti"

def Create_Plot():
    global ds
    TOOLTIPS = [
        ("Nama", "@x"),
        ("Number", "@y"),
    ]
    p = figure(x_range=ds.data['x'], height=250, title="Percobaan Benua",sizing_mode="stretch_both",tooltips=TOOLTIPS)
    p.vbar(x='x', top='y', width=0.9, source=ds)
    p.xgrid.grid_line_color = None
    p.xaxis.major_label_orientation = "vertical"
    return p
    

region_select.on_change('value',Handle_Change_Dropdown)
country_select.on_change('value',Handle_Change_Dropdown)
colums_select.on_change('value',Handle_Change_Dropdown)


#init figure All
plt = Create_Plot()

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



# def Create_Plot(ds,region, country, case):
#     TOOLTIPS = [
#         ("Nama", "@x"),
#         ("Number", "@y"),
#     ]
#     # Orientation = "vertical"
#     # if region != "All":
#     #     temp = df[df["WHO Region"] == region]
#     #     ds = ColumnDataSource(temp)
#     # else :
#     #     ds = ColumnDataSource(df)
    
#     # if country != "All":
#     #     result = np.where(ds.data['Country/Region'] == country)
#     #     data = dict(x = ds.data['Country/Region'][result[0]], y = ds.data[case][result[0]])
#     #     maxyrange = data["y"][0]
#     #     Orientation = "horizontal"
#     # else :
#     #     data = dict(x = ds.data['Country/Region'], y = ds.data[case])
#     #     maxyrange = 100000
        

#     p = figure(x_range=ds.data['x'], y_range=(0,100000), height=250, title="Percobaan Benua",sizing_mode="stretch_both",tooltips=TOOLTIPS)
#     p.vbar(x='x', top='y', width=0.9, source=ds)
#     p.xgrid.grid_line_color = None
#     p.xaxis.major_label_orientation = "vertical"
#     return p

# js_on_change_region = CustomJS(args=dict(plt=plt), code="""plt.reset.emit(); console.log("Berhasil")""")
# country_select.js_on_change('value', js_on_change_region)
# print(type(ds.data['x']))
# print(ds.data['x'])
# test = ds.data['x'].loc[ds.data['x'] == 'Angola']
# print(df[df['Country/Region'] == "Angola"])
# test = df[df['Country/Region'] == "Angola"]
# data = {
#     "x" : test['Country/Region'],
#     "y" : test[case]
# }

# TOOLTIPS = [
#     ("Nama", "@x"),
#     ("Number", "@y"),
# ]
# p = figure(x_range=ds.data['x'], y_range=(0,100000), height=250, title="Percobaan Benua",sizing_mode="stretch_both",tooltips=TOOLTIPS)
# p.vbar(x='x', top='y', width=0.9, source=ds)
# p.xgrid.grid_line_color = None

# kode="""
#     source.data['y'] = df[cb_obj.value];
#     source.change.emit();
# """

# callback = CustomJS(args={"df": df ,"source": ds}, code=kode)
# colums_select.js_on_change('value', callback)

    