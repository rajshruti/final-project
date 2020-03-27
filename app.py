import os
import pandas as pd
import requests
import xlrd
import matplotlib.pyplot as plt
from datetime import datetime, date, timedelta
from sqlalchemy import create_engine
from flask import Flask, jsonify, render_template
import dropout_predictions
import psycopg2


app = Flask(__name__)
conn = psycopg2.connect(user="postgres", password="root123", host="localhost", port="5432", database="admissions")

@app.route("/")
def home():
    return render_template("index.html")
@app.route("/admissions")
def admissions():
    return render_template("admissions.html")
@app.route("/stdntservices")
def stdntservices():
    return render_template("stdntservices.html")
@app.route("/finance")
def finance():
    return render_template("finance.html")

if __name__ == "__main__":
    app.run()