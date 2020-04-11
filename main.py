#!/usr/bin/python

'''
https://pythonhow.com/adding-more-pages-to-the-website/
'''

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/Africa/')
def Q1():
    return render_template('Africa.html')

@app.route('/Asia/')
def Q2():
    return render_template('Asia.html')

@app.route('/Europe/')
def Q3():
    return render_template('Europe.html')

@app.route('/NorthAmerica/')
def Q4():
    return render_template('NorthAmerica.html')

@app.route('/SouthAmerica/')
def Q5():
    return render_template('SouthAmerica.html')

@app.route('/Oceania/')
def Q6():
    return render_template('Oceania.html')


if __name__ == '__main__':
    app.run(debug=True)