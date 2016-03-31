# coding: utf-8

from datetime import datetime

from flask import Flask
from flask import render_template

app = Flask(__name__)

# 动态路由

@app.route('/')
def index():
    return str(datetime.now())

