import os
import re
import random
import cv
from fnmatch import fnmatch
from flask import Flask, jsonify
# from flask_cors import CORS
from flask import jsonify

app = Flask(__name__)
# CORS(app)
hits = 0

@app.route("/stats/")
@app.route("/stats")
def stats():
    global hits
    return(str(hits))
    
    
@app.route("/<name>/")
def check_version(name):
    global hits
    hits += 1
    software = []
    software.append(name)
    version = cv.check_versions_api(software)
    software, ver, date, link , description = version
    if ver == "": return(f"No software matching {name} found!")
    response = { 'version': ver, 'description': description, 'name': software,'release date':date, 'link': link}
    
    return jsonify(response)


def human_format(num):
    magnitude = 0
    while abs(num) >= 1000:
        magnitude += 1
        num /= 1000.0
    # add more suffixes if you need them
    return '%.1f%s' % (num, ['', 'K', 'M', 'G', 'T', 'P'][magnitude])

if __name__ == "__main__":

    app.run(host='0.0.0.0', port=8889)