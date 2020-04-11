#!/usr/bin/python

import pycountry_convert as pc
import pandas as pd
import requests
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

#  To avoid unwanted float values
pd.options.display.float_format = '{:,.0f}'.format

url = 'https://www.worldometers.info/coronavirus/'

#  To avoid 403 Error
header = {
  "User-Agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.75 Safari/537.36",
  "X-Requested-With": "XMLHttpRequest"
}

r = requests.get(url, headers=header)

df = pd.read_html(r.text)
df = df[0]
df = df[1:212]

df.columns = ['Country','TotalCases','NewCases','TotalDeaths','NewDeaths','TotalRecovered','ActiveCases','Critical','Tot Cases/1M pop','Deaths/1M pop','	TotalTests','Tests/ 1M pop']

#  Replace few countries names

df = df.replace(to_replace ="UK", value ="United Kingdom")
df = df.replace(to_replace ='S. Korea', value ="South Korea")
df = df.replace(to_replace ='UAE', value ="United Arab Emirates")
df = df.replace(to_replace ='0', value =0)

#  filling missing values by 0
df = df.fillna('0')

#  function to find continent for relevant country
def country_to_continent(country_name):
  country_alpha2 = pc.country_name_to_country_alpha2(country_name)
  country_continent_code = pc.country_alpha2_to_continent_code(country_alpha2)
  country_continent_name = pc.convert_continent_code_to_continent_name(country_continent_code)
  return country_continent_name

country = df['Country'].to_list()
continent = []

#  Adding continent
for c in country:
    try:
        continent.append(country_to_continent(c))
    except Exception as err:
        continent.append('Others')

#  Added continent as second column
df.insert(1,'Continent',continent)

df.to_csv('data.csv',index=False)
df = pd.read_csv('data.csv')

#  segregating each rows values by continents
Africa = df[df['Continent'] == 'Africa']
Asia = df[df['Continent'] == 'Asia']
Europe  = df[df['Continent'] == 'Europe']
North_America  = df[df['Continent'] == 'North America']
Others = df[df['Continent'] == 'Others']
South_America  = df[df['Continent'] == 'South America']
Oceania  = df[df['Continent'] == 'Oceania']

def gen_template(dataframe,outputfile,w,h):

    output_file(outputfile)

    df_table = DataTable(
        columns=[TableColumn(field=Ci, title=Ci) for Ci in dataframe.columns],
        source=ColumnDataSource(dataframe),
        width=1500,
        height=200,
    )

    x = dataframe[['Country','TotalCases']]
    i = x.sort_values("TotalCases", axis=0, ascending=False)
    i = pd.DataFrame(i).set_index("Country")
    i_bar = i.plot_bokeh(kind="bar",ylabel="Total Cases",title="",show_figure=False,color='orange')

    y = dataframe[['Country','TotalDeaths']]
    j = y.sort_values("TotalDeaths", axis=0, ascending=False)
    j = pd.DataFrame(j).set_index("Country")
    j_bar = j.plot_bokeh(kind="bar",ylabel="Total Deaths",title="",show_figure=False,color='red')

    pandas_bokeh.plot_grid([[df_table],[i_bar],[j_bar]],plot_width=w,plot_height=h)

# html template generation

gen_template(South_America,'SA.html',1000,500)
gen_template(Others,'O.html',1800,500)
gen_template(Oceania,'OC.html',1000,500)
gen_template(Africa,'A.html',4500,500)
gen_template(Asia,'As.html',4500,500)
gen_template(North_America,'NA.html',4500,500)
gen_template(Europe,'EU.html',4500,500)
