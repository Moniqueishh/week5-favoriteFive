
from app import app

from flask import render_template


@app.route('/')
def homePage():
    return render_template('index.html')

@app.route('/favoritefive')
def favoriteFive():
    favorite = [
            {
            "name" : "The 1975"
            },
            {
            "name" : "Hozier"
            },
            {
            "name" : "Jesse Reyez"
            },
            {
            "name" : "Omar Apollo"
            },
            {
            "name" : "Kali Uchis"
            }
        ]
    return render_template("favoritefive.html", favorite=favorite)

@app.route('/login')
def loginPage():
    return render_template('login.html')