#!/usr/bin/env python

import os
from os import walk
import csv
from flask import Flask, request, send_from_directory
from collections import defaultdict

app = Flask(__name__)
app.secret_key = '2d9-E2.(f&é,P$p@fpb+zSU03êû9_'

@app.route('/')
def home():
    return "Try: '/refresh', '/get', /get/{index}', '/get/{index}/image'. If there is no csv file, try to access '/refresh'"

@app.route('/refresh/')
def refresh():
    try:
        files = []
        for (dirpath, dirnames, filenames) in walk('./images'):
            files.extend(filenames)
            break
        with open('file.csv', 'w', newline='') as csvfile:
            fieldnames = ['id', 'filename']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            ids = 1
            for elem in files:
                writer.writerow({'id': ids, 'filename': elem})
                ids += 1
        return "Success"
    except OSError:
        return "An error occured"

@app.route('/get/')
def get():
    try:
        with open('file.csv') as csv_file:
            csv_reader = csv.DictReader(csv_file)
            columns = defaultdict(list)
            for row in csv_reader:
                for (i, j) in row.items():
                    columns[i].append(j)
            return "{}".format(columns['id'])
    except OSError:
        return "An error occured"

@app.route('/get/<int:num>/')
def get_index(num):
    try:
        with open('file.csv') as f:
            reader = csv.reader(f)
            line = 0
            for row in reader:
                if line != 0:
                    if line == num:
                       return "{}".format(row)
                line += 1
            return "Error: try '/get' to see the index valable"
    except OSError:
        return "An error occured"

@app.route('/get/<int:num>/image/')
def get_image(num):
    try:
        with open('file.csv') as f:
            reader = csv.DictReader(f)
            line = 0
            imgName = ''
            for row in reader:
                if line == num - 1:
                    imgName = (row['filename'])
                line += 1
            if imgName == '':
                return "Index not found. Try '/get'"
            return send_from_directory(app.static_folder, './images/' + imgName, mimetype='image/jpg')
    except OSError:
        return "An error occured"
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)
