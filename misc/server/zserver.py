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


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/auth/login', methods=['POST', 'GET'])
def auth_login():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]
        if valid_login(username, password):
            print "correct user"
            return redirect(url_for('admin_view'))
        else:
            print "wrong user"
            return redirect(url_for('auth_login'))
    else:
        return render_template('auth_login.html')
@app.route('/auth/logout', methods=['GET'])
def auth_logout():
    # clear cookie
    return render_template('index.html')


@app.route('/admin/view', methods=['POST', 'GET'])
def admin_view ():
    return render_template('admin_view.html')

def valid_login(username, password):
    if username == "admin" and password == "admin":
        return True
    else:
        return False

@app.route('/monitor/free')
def monitor_top():
    output = os.popen("free")
    return output.read().replace('\n', '</br>')






if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0')

