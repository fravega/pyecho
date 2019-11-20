#!/usr/local/bin/python3
import os
from flask import Flask, request
from flask import jsonify
import sys

app = Flask(__name__)

@app.route("/")
def echo ():

    return "echo ok\n"

@app.route('/test', methods = ['POST', 'GET'])
def test():
    if request.method == 'POST':
       print (request.is_json)
       content = request.get_json()
       print (content,file=sys.stderr)
     

       return "POST ok"
    else:
       return "GET ok"


if __name__ == '__main__':

    app.run(debug=os.environ['FLASK_ENV'] == 'development',host='0.0.0.0', port=8080)
