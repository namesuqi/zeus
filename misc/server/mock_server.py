# coding=utf-8
"""
TODO: Add description for file

__author__ = 'zengyuetian'

"""


from flask import Flask
from flask import render_template
import os
from flask import url_for
from flask import request
from flask import redirect
from flask import make_response
from flask import json
from flask import jsonify

import subprocess

app = Flask(__name__)


hit = 0

@app.route('/')
def index():
    global hit
    hit += 1
    if hit%100 == 0:
        print("                                                           %s" %(hit))
    return "OK"







if __name__ == '__main__':
    # app.debug = True
    app.run(host='0.0.0.0')

