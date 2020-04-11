#!/usr/bin/python

import pandas as pd
from bokeh.models.widgets import DataTable, DateFormatter, TableColumn
from bokeh.io import output_file,show
import pandas_bokeh
from pandas_bokeh import plot_bokeh
from bokeh.models import ColumnDataSource

from math import pi

from bokeh.palettes import Category20c
from bokeh.plotting import figure
from bokeh.transform import cumsum
import sys

'''
https://github.com/PatrikHlobil/Pandas-Bokeh
https://www.worldometers.info/world-population/population-by-country/
http://docs.bokeh.org/en/latest/docs/gallery/pie_chart.html
'''

corona_df = pd.read_html('https://www.worldometers.info/coronavirus/')

def gen_template_1(outputfile):

    df = corona_df[0]
    #df = df[['Country,Other','TotalCases']]
    df = df.head(21)
    df = df.fillna(method='ffill')
    data_table = DataTable(
        columns=[TableColumn(field=Ci,title=Ci) for Ci in df.columns],
        source=ColumnDataSource(df),
        width=800,
    )
    df = pd.DataFrame(df).set_index("Country,Other")
    bar_graph = df.plot_bokeh.barh(xlabel='TotalCases Count', ylabel='Country', show_figure=False)
    pandas_bokeh.plot_grid([[data_table, bar_graph]], plot_width=800, plot_height=350)

#gen_template_1('corono.html')


#########################################################################################

output_file("pie.html")

gdp = pd.read_html('https://www.worldometers.info/gdp/gdp-by-country/')
gdp = gdp[0]
gdp.columns = ['#','Country','GDP_nominal_2017','GDP_abbrev','GDP_Growth','Population_2017','GDP_per_Capita','Share_of_World_GDP']
gdp = gdp.head(20)

gdp_table = DataTable(
    columns=[TableColumn(field=Ci, title=Ci) for Ci in gdp.columns],
    source=ColumnDataSource(gdp),
    width=900,
)

gdp_df = gdp[['Country','GDP_nominal_2017','GDP_abbrev']]
data = gdp_df.rename(columns={'index':'Country'})
l = data['GDP_nominal_2017'].to_list()
l = [sub.replace('$', '').replace(',', '') for sub in l]
l = [int(i) for i in l]
l = pd.Series(l)
data['angle'] = l/l.sum() * 2*pi
data['color'] = Category20c[len(gdp)]

p = figure(plot_height=350, title="World GDP Distribution", toolbar_location='above',
            tooltips="@Country:" + "@GDP_abbrev", x_range=(-0.5, 1.0))

p.wedge(x=0, y=1, radius=0.4,
        start_angle=cumsum('angle', include_zero=True), end_angle=cumsum('angle'),
        line_color="white", fill_color='color', legend_field='Country', source=data)

p.axis.axis_label=None
p.axis.visible=False
p.grid.grid_line_color = None

pandas_bokeh.plot_grid([[gdp_table,p]])





