# Python_based_Dashboard
Python based Dashboard using (Pandas + Pandas-Bokeh + Flask). Useful in creating interactive Dashboard for data analysis,reporting. <br>

REFERENCE:<br>
'''<br>
https://github.com/PatrikHlobil/Pandas-Bokeh<br>
https://www.worldometers.info/world-population/population-by-country/<br>
http://docs.bokeh.org/en/latest/docs/gallery/pie_chart.html<br>
https://pythonhow.com/adding-more-pages-to-the-website/<br>
'''<br>

1) gen_dash_html.py file : will request COVID-19 URL and fetch dataset. We'll make necessary changes to the dataset. We'll map each country to the continent and then segregate each continent. It will generate dynamic html files for each continent. Add {% extends "layout.html" %}
{% block content %} top and {% endblock %} bottom of each generated dynamic html files. 
2) Place all html files in a templates folder and style.css file in static/css folder. Make changes in home.html, layout.html ,layout2.html and main.py only if required. <br>
3) Run ./main.py to make dashboard live.<br>
4) Entire source code is 'dashboard.zip' zipped for reference.
