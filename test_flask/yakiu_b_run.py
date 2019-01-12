# -*- coding: utf-8 -*-
import numpy as np
import pandas as pd
import requests
import json
import sys

# Import database module.
import pyrebase
config = {
    "apiKey": "AIzaSyBtXlXdTSty5El0Xacn0CXlIorKVtqesxg",
    "authDomain": "baseball-test-d74f9.firebaseapp.com",
    "databaseURL": "https://baseball-test-d74f9.firebaseio.com",
    "projectId": "baseball-test-d74f9",
    "storageBucket": "baseball-test-d74f9.appspot.com",
    "messagingSenderId": "886862023113"
}
firebase = pyrebase.initialize_app(config)

db = firebase.database()
data = {"name": "Mortimer 'Morty' Smith"}
db.child("users").push(data)
print('hello')
users = db.child("comments").get()
print(users.val())
print('world')

df_m = pd.read_csv('data/to_csv_out2.csv')
df_dic = df_m.to_dict(orient='records')

df_tutu = pd.read_csv('data/to_csv_tutu_year.csv')
df_tutu = df_tutu.to_dict(orient='records')

from flask import Flask,render_template, render_template, request
app = Flask(__name__)

@app.route('/')
def test2():
    data1 = df_dic
    return render_template('index3.html', data1=data1)

@app.route('/tutu')
def tutu():
    data1 = df_tutu
    return render_template('tutu.html', data1=data1)

if __name__ == '__main__':
    app.run()


