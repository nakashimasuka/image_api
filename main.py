#!/usr/bin/env python

import os
from os import walk
import csv
from flask import Flask

app = Flask(__name__)
app.secret_key = '2d9-E2.(f&é,P$p@fpb+zSU03êû9_'

@app.route('/')
def index():
    return "Try: '/refresh', '/get', /get/{index}', '/get/{index}/image'"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
